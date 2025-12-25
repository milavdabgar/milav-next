"use client";

import React, { useEffect, useRef, useState } from 'react';

interface MermaidProps {
    children?: string;
}

import { useTheme } from 'next-themes';

export function Mermaid({ children }: MermaidProps) {
    const elementRef = useRef<HTMLDivElement>(null);
    const [isRendered, setIsRendered] = useState(false);
    const { theme, systemTheme } = useTheme();

    useEffect(() => {
        const loadMermaid = async () => {
            try {
                // Dynamically import mermaid to avoid SSR issues
                const mermaid = (await import('mermaid')).default;

                const currentTheme = theme === 'system' ? systemTheme : theme;
                const mermaidTheme = currentTheme === 'dark' ? 'dark' : 'default';

                mermaid.initialize({
                    startOnLoad: false,
                    theme: mermaidTheme,
                    securityLevel: 'loose',
                    fontFamily: 'inherit',
                });

                if (!children || !children.trim()) {
                    return;
                }

                if (elementRef.current) {
                    // Clear previous content
                    elementRef.current.innerHTML = '';
                    elementRef.current.removeAttribute('data-processed'); // Help mermaid re-render content if needed

                    // Generate unique ID
                    const id = `mermaid-${Math.random().toString(36).substr(2, 9)}`;

                    // Render mermaid diagram
                    try {
                        const { svg } = await mermaid.render(id, children.trim());
                        elementRef.current.innerHTML = svg;
                        setIsRendered(true);
                    } catch (renderError) {
                        console.error('Failed to render mermaid:', renderError);
                        elementRef.current.innerHTML = `<div class="text-red-500 p-2 text-sm border border-red-200 rounded bg-red-50">Invalid Mermaid syntax</div>`;
                    }
                }
            } catch (error) {
                console.error('Error rendering Mermaid diagram:', error);
            }
        };

        loadMermaid();
    }, [children, theme, systemTheme]);

    return (
        <div
            ref={elementRef}
            className={`flex justify-center my-6 overflow-x-auto ${isRendered ? 'opacity-100' : 'opacity-0'} transition-opacity duration-300`}
        />
    );
}
