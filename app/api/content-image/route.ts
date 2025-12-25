
import { NextRequest, NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';
import mime from 'mime';

export async function GET(request: NextRequest) {
    const searchParams = request.nextUrl.searchParams;
    let relativePath = searchParams.get('path');

    // Fallback: If no path param, try to use the pathname from the URL
    // This handles the case where the request is rewritten from /resources/... and we want to Map it to content/resources/...
    if (!relativePath) {
        const pathname = request.nextUrl.pathname;
        // If the request isn't directly to the API endpoint, assume the pathname is the file path
        if (!pathname.startsWith('/api/')) {
            relativePath = pathname.startsWith('/') ? pathname.substring(1) : pathname;
        }
    }

    if (!relativePath) {
        return new NextResponse('Path parameter is required', { status: 400 });
    }

    // Security check: ensure path starts with 'content/' (or relative to it, depending on how we construct it)
    // The rewrite passes "resources/study-materials/...", so we prepend "content/"
    const fullPath = path.join(process.cwd(), 'content', relativePath);

    // Security check: Ensure we are not traversing out of the content directory
    const contentDir = path.join(process.cwd(), 'content');
    if (!fullPath.startsWith(contentDir)) {
        return new NextResponse('Invalid path', { status: 403 });
    }

    if (!fs.existsSync(fullPath)) {
        return new NextResponse('File not found', { status: 404 });
    }

    if (fs.statSync(fullPath).isDirectory()) {
        return new NextResponse('Path is a directory', { status: 400 });
    }

    const fileBuffer = fs.readFileSync(fullPath);
    const contentType = mime.getType(fullPath) || 'application/octet-stream';

    return new NextResponse(fileBuffer, {
        headers: {
            'Content-Type': contentType,
            'Cache-Control': 'public, max-age=31536000, immutable',
        },
    });
}
