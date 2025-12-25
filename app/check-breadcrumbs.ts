
import { getBreadcrumbs } from '@/lib/breadcrumbs';
import { getContentBySlug } from '@/lib/mdx';

async function test() {
    console.log('--- Testing getContentBySlug ---');
    const folder = 'resources/study-materials/16-it';
    const slug = '_index';

    try {
        const content = getContentBySlug(folder, slug);
        console.log(`Checking ${folder}/${slug}:`, content ? content.metadata.title : 'NULL');
    } catch (e) {
        console.error('Error in getContentBySlug:', e);
    }

    console.log('\n--- Testing getBreadcrumbs ---');
    try {
        const breadcrumbs = getBreadcrumbs('resources/study-materials', ['16-it', 'sem-1']);
        console.log('Breadcrumbs generated:', JSON.stringify(breadcrumbs, null, 2));
    } catch (e) {
        console.error('Error in getBreadcrumbs:', e);
    }
}

test();
