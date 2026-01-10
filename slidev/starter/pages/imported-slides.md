# Imported Slides

You can split your slides.md into multiple files and organize them as you want using the `src` attribute.

#### `slides.md`

```markdown
# Page 1

Page 2 from main entry.

---

## src: ./subpage.md
```

<br>

#### `subpage.md`

```markdown
# Page 2

Page 2 from another file.
```

[Learn more](https://sli.dev/guide/syntax.html#importing-slides)

<!--
Dr. James: Here's a powerful organizational feature that becomes essential as your presentations grow in complexity - imported slides. This allows you to split your presentation into multiple files for better maintainability.

Sarah: Notice how clean this approach is. In your main slides.md file, you simply use the src attribute to reference external slide files. This modular approach is perfect for large presentations, team collaboration, or when you want to reuse slide sections across multiple presentations.

Dr. James: The subpage.md file contains its own slide content that gets seamlessly integrated into your main presentation flow. This means you can have different team members working on different sections simultaneously, or organize your slides by topic or chapter.

Sarah: This feature is particularly valuable for documentation-heavy presentations, training materials, or any scenario where you need to maintain a large slide deck over time. It keeps your files manageable and your content organized.
-->
