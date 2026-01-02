import { NextResponse } from 'next/server';

export async function GET() {
  return NextResponse.json({
    status: 'ok',
    timestamp: new Date().toISOString(),
    service: 'milav-next',
    version: process.env.GIT_COMMIT || 'unknown',
  });
}
