FROM node:24-alpine AS deps
# Install libc compatibility for better package support
RUN apk add --no-cache libc6-compat
WORKDIR /app

# Install dependencies based on the preferred package manager
COPY package.json package-lock.json* ./
# Use legacy peer deps to handle dependency conflicts
RUN npm ci --omit=dev --legacy-peer-deps --no-fund --quiet --no-audit

# Rebuild the source code only when needed
FROM node:24-alpine AS builder
WORKDIR /app

# Install build dependencies for native modules
RUN apk add --no-cache \
    python3 \
    make \
    g++ \
    cairo-dev \
    jpeg-dev \
    pango-dev \
    musl-dev \
    giflib-dev \
    pixman-dev \
    pangomm-dev \
    libjpeg-turbo-dev \
    freetype-dev \
    && rm -rf /var/cache/apk/* /tmp/* /var/tmp/*

COPY package.json package-lock.json* ./
# Install all dependencies including dev dependencies for build
RUN npm ci --legacy-peer-deps --no-fund --quiet --no-audit
COPY . .

# Disable Next.js telemetry
ENV NEXT_TELEMETRY_DISABLED=1
# Set your base URL - update this to your actual domain
ENV NEXT_PUBLIC_BASE_URL=https://milav.gppalanpur.ac.in

RUN npm run build

# Production image, copy all the files and run next
FROM node:24-alpine AS runner
WORKDIR /app

ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED=1

# Install runtime dependencies for document processing (pandoc, LaTeX)
RUN apk add --no-cache \
    chromium \
    nss \
    freetype \
    harfbuzz \
    ca-certificates \
    ttf-freefont \
    pandoc \
    texlive-full \
    # Essential fonts for better typography  
    ttf-liberation \
    ttf-dejavu \
    font-noto \
    && rm -rf /var/cache/apk/* /tmp/* /var/tmp/*

# Verify LaTeX installation works at runtime
RUN echo '\documentclass{article}\usepackage{xcolor}\usepackage{amsmath}\begin{document}\textcolor{blue}{LaTeX Works!} $E=mc^2$\end{document}' > /tmp/test.tex && \
    xelatex -output-directory=/tmp /tmp/test.tex && \
    pdflatex -output-directory=/tmp /tmp/test.tex && \
    lualatex -output-directory=/tmp /tmp/test.tex && \
    rm -rf /tmp/*

# Set Puppeteer to use the installed Chromium
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true \
    PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

COPY --from=builder /app/public ./public

# Set the correct permission for prerender cache
RUN mkdir .next
RUN chown nextjs:nodejs .next

# Automatically leverage output traces to reduce image size
# https://nextjs.org/docs/advanced-features/output-file-tracing
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

# Copy content directory for MDX files
COPY --from=builder --chown=nextjs:nodejs /app/content ./content

USER nextjs

EXPOSE 3000

ENV PORT=3000
ENV HOSTNAME="0.0.0.0"

CMD ["node", "server.js"]
