
import { NextRequest, NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';
import mime from 'mime';

export async function GET(request: NextRequest) {
    try {
        const { searchParams } = new URL(request.url);
        const filePath = searchParams.get('path');

        if (!filePath) {
            return NextResponse.json(
                { error: 'Path is required' },
                { status: 400 }
            );
        }

        // Security check: Ensure path is within content directory
        // We expect filePath to be relative to 'content/resources' or just 'content'
        // Let's explicitly require it to be relative to 'content' for now, but usually it comes as slug path.
        // Actually, let's assume valid paths start with 'resources' for now or generic content.

        // Normalize and resolve path
        const contentDir = path.resolve(process.cwd(), 'content');
        const absolutePath = path.resolve(contentDir, filePath);

        // Prevent directory traversal
        if (!absolutePath.startsWith(contentDir)) {
            return NextResponse.json(
                { error: 'Invalid path' },
                { status: 403 }
            );
        }

        if (!fs.existsSync(absolutePath)) {
            return NextResponse.json(
                { error: 'File not found' },
                { status: 404 }
            );
        }

        const stat = fs.statSync(absolutePath);
        if (!stat.isFile()) {
            return NextResponse.json(
                { error: 'Not a file' },
                { status: 400 }
            );
        }

        const fileBuffer = fs.readFileSync(absolutePath);
        const contentType = mime.getType(absolutePath) || 'application/octet-stream';
        const filename = path.basename(absolutePath);

        return new NextResponse(fileBuffer, {
            headers: {
                'Content-Type': contentType,
                'Content-Disposition': `inline; filename="${filename}"`,
                'Cache-Control': 'public, max-age=3600'
            }
        });

    } catch (error) {
        console.error('File serve error:', error);
        return NextResponse.json(
            { error: 'Internal server error' },
            { status: 500 }
        );
    }
}
