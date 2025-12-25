import * as React from "react"
import { Card, CardContent } from "@/components/ui/card"
import {
    Carousel,
    CarouselContent,
    CarouselItem,
    CarouselNext,
    CarouselPrevious,
} from "@/components/ui/carousel"
import Image from "next/image"

interface CarouselGalleryProps {
    images: string | string[];
    aspectRatio?: string;
}

export function CarouselGallery({ images, aspectRatio = "16-9" }: CarouselGalleryProps) {
    // Parse images if string
    const imageList = Array.isArray(images)
        ? images
        : images.split(',').map(src => src.trim()).filter(Boolean);

    // Fix paths: if path starts with 'images/', prepend '/portfolio/'
    // This is specific to the migration from Hugo where images were relative
    const fixedImages = imageList.map(src => {
        if (src.startsWith('images/')) {
            return `/portfolio/${src}`;
        }
        return src;
    });

    return (
        <div className="w-full max-w-4xl mx-auto my-8">
            <Carousel className="w-full">
                <CarouselContent>
                    {fixedImages.map((src, index) => (
                        <CarouselItem key={index}>
                            <div className="p-1">
                                <Card>
                                    <CardContent className="flex items-center justify-center p-0 overflow-hidden rounded-md bg-muted/20">
                                        <div className={`relative w-full ${aspectRatio === "16-9" ? "aspect-video" : "aspect-[4/3]"}`}>
                                            <Image
                                                src={src}
                                                alt={`Gallery image ${index + 1}`}
                                                fill
                                                className="object-contain"
                                                sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
                                            />
                                        </div>
                                    </CardContent>
                                </Card>
                            </div>
                        </CarouselItem>
                    ))}
                </CarouselContent>
                <CarouselPrevious />
                <CarouselNext />
            </Carousel>
        </div>
    )
}
