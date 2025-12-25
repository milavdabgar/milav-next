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
                const mermaidTheme = currentTheme === 'dark' ? 'base' : 'default';

                // Define theme variables to ensure high contrast in dark mode
                // User requested lighter background colors to make things easier
                const themeVariables = currentTheme === 'dark' ? {
                    primaryColor: '#e2e8f0', // slate-200 (Light nodes)
                    primaryTextColor: '#0f172a', // slate-900 (Dark text)
                    primaryBorderColor: '#94a3b8', // slate-400
                    lineColor: '#ffffff', // White (High contrast lines)
                    secondaryColor: '#f1f5f9', // slate-100
                    tertiaryColor: '#ffffff', // white
                    mainBkg: 'transparent', // Transparent background
                    nodeBorder: '#94a3b8', // slate-400
                    clusterBkg: '#1e293b', // slate-800
                    clusterBorder: '#cbd5e1', // slate-300
                    defaultLinkColor: '#ffffff', // White links
                    arrowheadColor: '#ffffff', // White arrowheads
                    titleColor: '#f8fafc', // Light title
                    edgeLabelBackground: '#1e293b', // Dark background for edge labels

                    // Additional overrides to force white lines
                    stroke: '#ffffff',
                    edgeStroke: '#ffffff',
                } : undefined;

                // Force CSS overrides to guarantee visibility
                // This targets the SVG internals directly to bypass any theme specificity issues
                const themeCSS = currentTheme === 'dark' ? `
                    .edgePath .path { stroke: #ffffff !important; }
                    .marker { fill: #ffffff !important; stroke: #ffffff !important; }
                    .flowchart-link { stroke: #ffffff !important; }
                ` : undefined;

                mermaid.initialize({
                    startOnLoad: false,
                    theme: mermaidTheme,
                    themeVariables,
                    themeCSS,
                    securityLevel: 'loose',
                    // Use standard system fonts to prevent width calculation errors where text gets chopped off
                    fontFamily: 'ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
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
