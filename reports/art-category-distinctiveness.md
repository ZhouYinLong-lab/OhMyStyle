# 艺术家、艺术流派与艺术学院差异审查

> 2026-10-20 更新。逐项检查了三个分类的全部包摘要、关系签名和横版代表图。图像筛查使用感知哈希、色彩分布、明度、纹理和布局信号；它只产生人工复核候选，不代表语义重复。

## 覆盖范围

- 艺术家：83 包；艺术流派：87 包；艺术学院：24 包；合计 194 包。
- 三类画廊的类内比较 7,420 对、跨类比较 11,301 对，总计 18,721 对；相似度达到 0.82 的候选 101 对，其中艺术家类内 18 对、流派类内 13 对、学院类内 1 对，跨分类 69 对。
- 此次重新计算了全部 18,721 对，并逐张查看 101 对候选代表图。候选图之间没有发现明显的重复图像或足以合并风格包的视觉重复；部分候选共享低饱和度、室内静物或风景构图，但题材、媒介和可见形式仍有区别。
- 该结果只验收代表图与分类摘要的可辨识度，不等同于用新架构为 194 个包逐包生成了受控对照图，也不构成方向成熟度验收。新架构方向仍需按 [比较方案](design/art-style-pack-v2/comparison-plan.yaml) 逐项留存真实生成输入、输出和评审记录。
- 关系差异字段仍逐包保存在相关包的 `evaluation.yaml:image_audit.candidate_pairs`；前次补齐的 114 个空字段已纳入本次复核。

## 图像复核候选

| 分数 | 包 A | 包 B | 主要筛查信号 |
|---:|---|---|---|
| 0.926 | [`anna-ancher`](../style-packages/artists/anna-ancher/README.md) | [`pictorialism`](../style-packages/movements/pictorialism/README.md) | perceptual_hash 0.88, color 0.96, luminance 0.95, texture 0.99, layout 0.94 |
| 0.897 | [`jean-auguste-dominique-ingres`](../style-packages/artists/jean-auguste-dominique-ingres/README.md) | [`yale-school-of-art`](../style-packages/schools/yale-school-of-art/README.md) | perceptual_hash 0.81, color 0.96, luminance 1.00, texture 0.99, layout 0.92 |
| 0.881 | [`ivan-aivazovsky`](../style-packages/artists/ivan-aivazovsky/README.md) | [`yale-school-of-art`](../style-packages/schools/yale-school-of-art/README.md) | perceptual_hash 0.80, color 0.92, luminance 0.94, texture 0.99, layout 0.99 |
| 0.881 | [`caspar-david-friedrich`](../style-packages/artists/caspar-david-friedrich/README.md) | [`american-luminism`](../style-packages/movements/american-luminism/README.md) | perceptual_hash 0.80, color 0.91, luminance 0.98, texture 0.99, layout 0.96 |
| 0.865 | [`impressionism`](../style-packages/movements/impressionism/README.md) | [`minimalism`](../style-packages/movements/minimalism/README.md) | color 0.95, luminance 0.97, texture 0.99, layout 0.93 |
| 0.863 | [`chinese-literati-ink-painting`](../style-packages/movements/chinese-literati-ink-painting/README.md) | [`california-institute-of-the-arts`](../style-packages/schools/california-institute-of-the-arts/README.md) | color 0.94, luminance 0.84, texture 0.99, layout 0.98 |
| 0.863 | [`anna-ancher`](../style-packages/artists/anna-ancher/README.md) | [`titian`](../style-packages/artists/titian/README.md) | perceptual_hash 0.88, luminance 0.83, texture 0.98, layout 0.93 |
| 0.863 | [`francisco-de-zurbaran`](../style-packages/artists/francisco-de-zurbaran/README.md) | [`gothic`](../style-packages/movements/gothic/README.md) | color 0.99, luminance 0.95, texture 0.98, layout 0.99 |
| 0.862 | [`jmw-turner`](../style-packages/artists/jmw-turner/README.md) | [`design-academy-eindhoven`](../style-packages/schools/design-academy-eindhoven/README.md) | color 0.95, luminance 0.95, texture 0.96, layout 0.97 |
| 0.859 | [`jan-van-eyck`](../style-packages/artists/jan-van-eyck/README.md) | [`northern-renaissance`](../style-packages/movements/northern-renaissance/README.md) | color 0.98, luminance 0.93, texture 0.99, layout 0.99 |
| 0.859 | [`francisco-de-zurbaran`](../style-packages/artists/francisco-de-zurbaran/README.md) | [`leonora-carrington`](../style-packages/artists/leonora-carrington/README.md) | color 0.93, luminance 0.87, texture 0.99, layout 1.00 |
| 0.858 | [`pictorialism`](../style-packages/movements/pictorialism/README.md) | [`romanticism`](../style-packages/movements/romanticism/README.md) | perceptual_hash 0.78, color 0.84, luminance 0.99, texture 1.00, layout 0.97 |
| 0.857 | [`johannes-vermeer`](../style-packages/artists/johannes-vermeer/README.md) | [`leonardo-da-vinci`](../style-packages/artists/leonardo-da-vinci/README.md) | color 0.97, luminance 0.97, texture 0.99, layout 1.00 |
| 0.856 | [`caravaggio`](../style-packages/artists/caravaggio/README.md) | [`titian`](../style-packages/artists/titian/README.md) | perceptual_hash 0.78, color 0.88, luminance 0.94, texture 0.98, layout 0.93 |
| 0.855 | [`anna-ancher`](../style-packages/artists/anna-ancher/README.md) | [`romanticism`](../style-packages/movements/romanticism/README.md) | color 0.89, luminance 0.96, texture 0.99, layout 0.97 |
| 0.854 | [`egon-schiele`](../style-packages/artists/egon-schiele/README.md) | [`chinese-literati-ink-painting`](../style-packages/movements/chinese-literati-ink-painting/README.md) | color 1.00, luminance 0.98, texture 1.00, layout 0.90 |
| 0.854 | [`utagawa-hiroshige`](../style-packages/artists/utagawa-hiroshige/README.md) | [`romanticism`](../style-packages/movements/romanticism/README.md) | color 0.87, luminance 0.97, texture 1.00, layout 0.92 |
| 0.853 | [`anna-ancher`](../style-packages/artists/anna-ancher/README.md) | [`futurism`](../style-packages/movements/futurism/README.md) | color 0.90, luminance 0.94, texture 0.97, layout 0.94 |
| 0.850 | [`conceptual-art`](../style-packages/movements/conceptual-art/README.md) | [`ulm-school`](../style-packages/schools/ulm-school/README.md) | color 1.00, luminance 1.00, texture 0.98, layout 0.92 |
| 0.849 | [`egon-schiele`](../style-packages/artists/egon-schiele/README.md) | [`california-institute-of-the-arts`](../style-packages/schools/california-institute-of-the-arts/README.md) | color 0.93, luminance 0.82, texture 1.00, layout 0.92 |
| 0.848 | [`rene-magritte`](../style-packages/artists/rene-magritte/README.md) | [`impressionism`](../style-packages/movements/impressionism/README.md) | color 0.90, luminance 0.95, texture 0.99, layout 0.96 |
| 0.848 | [`edgar-degas`](../style-packages/artists/edgar-degas/README.md) | [`rococo`](../style-packages/movements/rococo/README.md) | color 0.94, luminance 1.00, texture 1.00, layout 0.90 |
| 0.848 | [`claude-monet`](../style-packages/artists/claude-monet/README.md) | [`american-luminism`](../style-packages/movements/american-luminism/README.md) | color 0.94, luminance 0.99, texture 0.99, layout 0.82 |
| 0.848 | [`magic-realism`](../style-packages/movements/magic-realism/README.md) | [`northern-renaissance`](../style-packages/movements/northern-renaissance/README.md) | color 0.95, luminance 1.00, texture 0.99, layout 1.00 |
| 0.847 | [`art-deco`](../style-packages/movements/art-deco/README.md) | [`byzantine-art`](../style-packages/movements/byzantine-art/README.md) | color 0.97, luminance 1.00, texture 0.95, layout 0.95 |
| 0.844 | [`futurism`](../style-packages/movements/futurism/README.md) | [`neo-expressionism`](../style-packages/movements/neo-expressionism/README.md) | color 0.89, luminance 0.97, texture 0.99, layout 0.97 |
| 0.844 | [`jmw-turner`](../style-packages/artists/jmw-turner/README.md) | [`american-luminism`](../style-packages/movements/american-luminism/README.md) | color 0.82, luminance 0.95, texture 1.00, layout 0.98 |
| 0.843 | [`steampunk`](../style-packages/movements/steampunk/README.md) | [`victorian`](../style-packages/movements/victorian/README.md) | color 0.97, luminance 0.98, texture 0.99, layout 0.99 |
| 0.843 | [`american-luminism`](../style-packages/movements/american-luminism/README.md) | [`fluxus`](../style-packages/movements/fluxus/README.md) | color 0.92, luminance 0.92, texture 0.99, layout 0.88 |
| 0.843 | [`anna-ancher`](../style-packages/artists/anna-ancher/README.md) | [`lyrical-abstraction`](../style-packages/movements/lyrical-abstraction/README.md) | perceptual_hash 0.78, color 0.81, luminance 0.99, texture 0.99, layout 0.92 |
| 0.842 | [`kathe-kollwitz`](../style-packages/artists/kathe-kollwitz/README.md) | [`byzantine-art`](../style-packages/movements/byzantine-art/README.md) | color 0.91, luminance 0.94, texture 0.98, layout 0.93 |
| 0.841 | [`gustave-courbet`](../style-packages/artists/gustave-courbet/README.md) | [`pieter-bruegel-the-elder`](../style-packages/artists/pieter-bruegel-the-elder/README.md) | color 0.93, luminance 0.96, texture 0.99, layout 0.97 |
| 0.840 | [`jean-auguste-dominique-ingres`](../style-packages/artists/jean-auguste-dominique-ingres/README.md) | [`art-informel`](../style-packages/movements/art-informel/README.md) | color 0.93, luminance 0.99, texture 0.99, layout 0.90 |
| 0.839 | [`titian`](../style-packages/artists/titian/README.md) | [`pictorialism`](../style-packages/movements/pictorialism/README.md) | perceptual_hash 0.88, luminance 0.79, texture 0.99, layout 0.88 |
| 0.839 | [`caravaggio`](../style-packages/artists/caravaggio/README.md) | [`leonora-carrington`](../style-packages/artists/leonora-carrington/README.md) | color 0.94, luminance 0.92, texture 0.99, layout 0.98 |
| 0.839 | [`caravaggio`](../style-packages/artists/caravaggio/README.md) | [`northern-renaissance`](../style-packages/movements/northern-renaissance/README.md) | color 0.98, luminance 0.88, texture 0.99, layout 0.99 |
| 0.838 | [`caravaggio`](../style-packages/artists/caravaggio/README.md) | [`synthwave`](../style-packages/movements/synthwave/README.md) | color 0.93, luminance 0.91, texture 0.96, layout 1.00 |
| 0.838 | [`sofonisba-anguissola`](../style-packages/artists/sofonisba-anguissola/README.md) | [`glasgow-school-of-art`](../style-packages/schools/glasgow-school-of-art/README.md) | color 0.97, luminance 0.98, texture 0.98, layout 1.00 |
| 0.838 | [`diego-velazquez`](../style-packages/artists/diego-velazquez/README.md) | [`kathe-kollwitz`](../style-packages/artists/kathe-kollwitz/README.md) | color 0.94, luminance 0.84, texture 0.97, layout 0.99 |
| 0.838 | [`kawaii`](../style-packages/movements/kawaii/README.md) | [`new-bauhaus`](../style-packages/schools/new-bauhaus/README.md) | perceptual_hash 0.81, color 0.94, texture 0.99 |
| 0.836 | [`jean-auguste-dominique-ingres`](../style-packages/artists/jean-auguste-dominique-ingres/README.md) | [`black-mountain-college`](../style-packages/schools/black-mountain-college/README.md) | color 0.94, luminance 0.98, texture 0.95, layout 0.96 |
| 0.836 | [`artemisia-gentileschi`](../style-packages/artists/artemisia-gentileschi/README.md) | [`diego-velazquez`](../style-packages/artists/diego-velazquez/README.md) | color 1.00, luminance 0.99, texture 0.98, layout 0.98 |
| 0.836 | [`utagawa-hiroshige`](../style-packages/artists/utagawa-hiroshige/README.md) | [`design-academy-eindhoven`](../style-packages/schools/design-academy-eindhoven/README.md) | color 0.95, luminance 0.99, texture 0.97, layout 0.98 |
| 0.836 | [`kazimir-malevich`](../style-packages/artists/kazimir-malevich/README.md) | [`suprematism`](../style-packages/movements/suprematism/README.md) | color 0.99, luminance 0.95, texture 0.99, layout 1.00 |
| 0.835 | [`wassily-kandinsky`](../style-packages/artists/wassily-kandinsky/README.md) | [`nihonga`](../style-packages/movements/nihonga/README.md) | color 0.85, luminance 0.91, texture 0.95, layout 0.99 |
| 0.834 | [`jmw-turner`](../style-packages/artists/jmw-turner/README.md) | [`royal-danish-academy`](../style-packages/schools/royal-danish-academy/README.md) | color 0.94, luminance 0.99, texture 0.97, layout 0.86 |
| 0.834 | [`frida-kahlo`](../style-packages/artists/frida-kahlo/README.md) | [`titian`](../style-packages/artists/titian/README.md) | luminance 1.00, texture 1.00, layout 0.95 |
| 0.834 | [`jmw-turner`](../style-packages/artists/jmw-turner/README.md) | [`romanticism`](../style-packages/movements/romanticism/README.md) | perceptual_hash 0.78, color 0.80, luminance 0.91, texture 0.99, layout 0.94 |
| 0.834 | [`romanticism`](../style-packages/movements/romanticism/README.md) | [`design-academy-eindhoven`](../style-packages/schools/design-academy-eindhoven/README.md) | color 0.88, luminance 0.96, texture 0.97, layout 0.91 |
| 0.834 | [`peter-paul-rubens`](../style-packages/artists/peter-paul-rubens/README.md) | [`sofonisba-anguissola`](../style-packages/artists/sofonisba-anguissola/README.md) | color 0.99, luminance 0.92, texture 0.99, layout 0.98 |
| 0.834 | [`titian`](../style-packages/artists/titian/README.md) | [`lyrical-abstraction`](../style-packages/movements/lyrical-abstraction/README.md) | perceptual_hash 0.80, luminance 0.83, texture 1.00, layout 0.98 |
| 0.833 | [`caravaggio`](../style-packages/artists/caravaggio/README.md) | [`francisco-de-zurbaran`](../style-packages/artists/francisco-de-zurbaran/README.md) | color 1.00, luminance 0.96, texture 0.98, layout 0.99 |
| 0.833 | [`gustave-moreau`](../style-packages/artists/gustave-moreau/README.md) | [`victorian`](../style-packages/movements/victorian/README.md) | color 0.99, luminance 0.96, texture 0.97, layout 0.98 |
| 0.833 | [`utagawa-hiroshige`](../style-packages/artists/utagawa-hiroshige/README.md) | [`impressionism`](../style-packages/movements/impressionism/README.md) | color 0.95, luminance 0.94, texture 1.00, layout 0.93 |
| 0.833 | [`chinese-literati-ink-painting`](../style-packages/movements/chinese-literati-ink-painting/README.md) | [`conceptual-art`](../style-packages/movements/conceptual-art/README.md) | color 0.99, luminance 0.90, texture 1.00, layout 0.89 |
| 0.833 | [`black-mountain-college`](../style-packages/schools/black-mountain-college/README.md) | [`yale-school-of-art`](../style-packages/schools/yale-school-of-art/README.md) | color 0.96, luminance 0.99, texture 0.96, layout 0.88 |
| 0.832 | [`conceptual-art`](../style-packages/movements/conceptual-art/README.md) | [`california-institute-of-the-arts`](../style-packages/schools/california-institute-of-the-arts/README.md) | color 0.97, luminance 0.94, texture 0.99, layout 0.90 |
| 0.832 | [`diego-velazquez`](../style-packages/artists/diego-velazquez/README.md) | [`art-deco`](../style-packages/movements/art-deco/README.md) | color 0.95, luminance 0.90, texture 0.94, layout 0.97 |
| 0.832 | [`francisco-de-zurbaran`](../style-packages/artists/francisco-de-zurbaran/README.md) | [`jan-van-eyck`](../style-packages/artists/jan-van-eyck/README.md) | color 0.99, luminance 0.90, texture 0.97, layout 0.96 |
| 0.832 | [`kathe-kollwitz`](../style-packages/artists/kathe-kollwitz/README.md) | [`art-deco`](../style-packages/movements/art-deco/README.md) | color 0.93, luminance 0.94, texture 0.97, layout 0.98 |
| 0.830 | [`jmw-turner`](../style-packages/artists/jmw-turner/README.md) | [`japandi`](../style-packages/movements/japandi/README.md) | color 0.83, luminance 0.97, texture 0.96, layout 0.96 |
| 0.830 | [`chinese-literati-ink-painting`](../style-packages/movements/chinese-literati-ink-painting/README.md) | [`ulm-school`](../style-packages/schools/ulm-school/README.md) | color 0.98, luminance 0.90, texture 0.98, layout 0.97 |
| 0.829 | [`claude-monet`](../style-packages/artists/claude-monet/README.md) | [`slade-school-of-fine-art`](../style-packages/schools/slade-school-of-fine-art/README.md) | color 0.88, luminance 0.98, texture 0.96, layout 0.96 |
| 0.829 | [`northern-renaissance`](../style-packages/movements/northern-renaissance/README.md) | [`glasgow-school-of-art`](../style-packages/schools/glasgow-school-of-art/README.md) | color 0.98, luminance 0.97, texture 1.00, layout 0.97 |
| 0.829 | [`magic-realism`](../style-packages/movements/magic-realism/README.md) | [`glasgow-school-of-art`](../style-packages/schools/glasgow-school-of-art/README.md) | color 0.98, luminance 0.97, texture 0.99, layout 0.97 |
| 0.828 | [`titian`](../style-packages/artists/titian/README.md) | [`northern-renaissance`](../style-packages/movements/northern-renaissance/README.md) | color 0.89, luminance 0.94, texture 0.96, layout 0.92 |
| 0.828 | [`eugene-delacroix`](../style-packages/artists/eugene-delacroix/README.md) | [`neue-sachlichkeit`](../style-packages/movements/neue-sachlichkeit/README.md) | color 0.95, luminance 0.96, texture 0.99, layout 1.00 |
| 0.828 | [`caravaggio`](../style-packages/artists/caravaggio/README.md) | [`sofonisba-anguissola`](../style-packages/artists/sofonisba-anguissola/README.md) | color 0.99, luminance 0.93, texture 1.00, layout 0.95 |
| 0.828 | [`agnes-martin`](../style-packages/artists/agnes-martin/README.md) | [`paul-klee`](../style-packages/artists/paul-klee/README.md) | color 0.87, luminance 0.97, texture 0.96, layout 0.95 |
| 0.828 | [`leonardo-da-vinci`](../style-packages/artists/leonardo-da-vinci/README.md) | [`yale-school-of-art`](../style-packages/schools/yale-school-of-art/README.md) | color 0.88, luminance 0.95, texture 0.99, layout 0.87 |
| 0.827 | [`paul-gauguin`](../style-packages/artists/paul-gauguin/README.md) | [`mexican-muralism`](../style-packages/movements/mexican-muralism/README.md) | color 0.95, luminance 0.96, texture 1.00, layout 1.00 |
| 0.827 | [`futurism`](../style-packages/movements/futurism/README.md) | [`pictorialism`](../style-packages/movements/pictorialism/README.md) | color 0.83, luminance 0.90, texture 0.96, layout 0.89 |
| 0.827 | [`futurism`](../style-packages/movements/futurism/README.md) | [`neoclassicism`](../style-packages/movements/neoclassicism/README.md) | color 0.83, luminance 0.99, texture 0.98, layout 0.94 |
| 0.827 | [`jan-van-eyck`](../style-packages/artists/jan-van-eyck/README.md) | [`glasgow-school-of-art`](../style-packages/schools/glasgow-school-of-art/README.md) | color 0.99, luminance 0.96, texture 0.99, layout 0.99 |
| 0.827 | [`futurism`](../style-packages/movements/futurism/README.md) | [`yale-school-of-art`](../style-packages/schools/yale-school-of-art/README.md) | color 0.87, luminance 0.97, texture 0.97, layout 0.95 |
| 0.827 | [`sofonisba-anguissola`](../style-packages/artists/sofonisba-anguissola/README.md) | [`harlem-renaissance`](../style-packages/movements/harlem-renaissance/README.md) | color 0.96, luminance 0.92, texture 1.00, layout 0.98 |
| 0.826 | [`jean-auguste-dominique-ingres`](../style-packages/artists/jean-auguste-dominique-ingres/README.md) | [`futurism`](../style-packages/movements/futurism/README.md) | color 0.92, luminance 0.98, texture 0.96, layout 0.97 |
| 0.826 | [`romanticism`](../style-packages/movements/romanticism/README.md) | [`black-mountain-college`](../style-packages/schools/black-mountain-college/README.md) | color 0.90, luminance 0.94, texture 0.94, layout 0.85 |
| 0.826 | [`caspar-david-friedrich`](../style-packages/artists/caspar-david-friedrich/README.md) | [`fluxus`](../style-packages/movements/fluxus/README.md) | color 0.88, luminance 0.90, texture 0.98, layout 0.83 |
| 0.826 | [`futurism`](../style-packages/movements/futurism/README.md) | [`black-mountain-college`](../style-packages/schools/black-mountain-college/README.md) | color 0.83, luminance 0.96, texture 0.99, layout 0.93 |
| 0.826 | [`francisco-goya`](../style-packages/artists/francisco-goya/README.md) | [`gustave-moreau`](../style-packages/artists/gustave-moreau/README.md) | color 0.98, luminance 0.96, texture 1.00, layout 0.94 |
| 0.826 | [`deconstructivist-architecture`](../style-packages/movements/deconstructivist-architecture/README.md) | [`slade-school-of-fine-art`](../style-packages/schools/slade-school-of-fine-art/README.md) | color 0.89, luminance 0.91, texture 0.99, layout 0.96 |
| 0.825 | [`diego-velazquez`](../style-packages/artists/diego-velazquez/README.md) | [`byzantine-art`](../style-packages/movements/byzantine-art/README.md) | color 0.96, luminance 0.90, texture 0.99, layout 0.91 |
| 0.825 | [`sofonisba-anguissola`](../style-packages/artists/sofonisba-anguissola/README.md) | [`titian`](../style-packages/artists/titian/README.md) | color 0.86, luminance 0.99, texture 0.98, layout 0.88 |
| 0.825 | [`claude-monet`](../style-packages/artists/claude-monet/README.md) | [`deconstructivist-architecture`](../style-packages/movements/deconstructivist-architecture/README.md) | color 0.85, luminance 0.93, texture 0.95, layout 0.92 |
| 0.825 | [`chinese-literati-ink-painting`](../style-packages/movements/chinese-literati-ink-painting/README.md) | [`kawaii`](../style-packages/movements/kawaii/README.md) | color 0.99, luminance 0.95, texture 0.99, layout 0.92 |
| 0.825 | [`socialist-realism`](../style-packages/movements/socialist-realism/README.md) | [`royal-academy-schools`](../style-packages/schools/royal-academy-schools/README.md) | color 0.89, luminance 0.97, texture 0.98, layout 0.97 |
| 0.824 | [`paul-gauguin`](../style-packages/artists/paul-gauguin/README.md) | [`titian`](../style-packages/artists/titian/README.md) | color 0.95, luminance 0.93, texture 0.98, layout 0.91 |
| 0.824 | [`gustave-moreau`](../style-packages/artists/gustave-moreau/README.md) | [`yale-school-of-art`](../style-packages/schools/yale-school-of-art/README.md) | perceptual_hash 0.78, color 0.84, texture 0.98, layout 0.89 |
| 0.823 | [`jean-auguste-dominique-ingres`](../style-packages/artists/jean-auguste-dominique-ingres/README.md) | [`leonardo-da-vinci`](../style-packages/artists/leonardo-da-vinci/README.md) | color 0.91, luminance 0.95, texture 1.00, layout 0.95 |
| 0.823 | [`anna-ancher`](../style-packages/artists/anna-ancher/README.md) | [`black-mountain-college`](../style-packages/schools/black-mountain-college/README.md) | color 0.95, luminance 0.98, texture 0.95, layout 0.88 |
| 0.823 | [`francisco-goya`](../style-packages/artists/francisco-goya/README.md) | [`symbolism`](../style-packages/movements/symbolism/README.md) | color 0.96, luminance 1.00, texture 0.98, layout 0.99 |
| 0.823 | [`titian`](../style-packages/artists/titian/README.md) | [`futurism`](../style-packages/movements/futurism/README.md) | color 0.82, luminance 0.89, texture 0.95, layout 0.99 |
| 0.822 | [`impressionism`](../style-packages/movements/impressionism/README.md) | [`situationist-international`](../style-packages/movements/situationist-international/README.md) | color 0.95, luminance 0.95, texture 0.97, layout 0.96 |
| 0.821 | [`caravaggio`](../style-packages/artists/caravaggio/README.md) | [`magic-realism`](../style-packages/movements/magic-realism/README.md) | color 0.93, luminance 0.87, texture 0.99, layout 0.99 |
| 0.821 | [`kawaii`](../style-packages/movements/kawaii/README.md) | [`suprematism`](../style-packages/movements/suprematism/README.md) | color 0.98, luminance 0.91, texture 0.97, layout 0.79 |
| 0.821 | [`romanticism`](../style-packages/movements/romanticism/README.md) | [`royal-academy-schools`](../style-packages/schools/royal-academy-schools/README.md) | color 0.83, luminance 0.96, texture 0.99, layout 0.87 |
| 0.821 | [`paul-klee`](../style-packages/artists/paul-klee/README.md) | [`neo-dada`](../style-packages/movements/neo-dada/README.md) | color 0.86, luminance 0.84, texture 0.99, layout 0.99 |
| 0.821 | [`sofonisba-anguissola`](../style-packages/artists/sofonisba-anguissola/README.md) | [`pictorialism`](../style-packages/movements/pictorialism/README.md) | perceptual_hash 0.78, color 0.86, luminance 0.79, texture 0.99 |
| 0.820 | [`mid-century-modern`](../style-packages/movements/mid-century-modern/README.md) | [`risd`](../style-packages/schools/risd/README.md) | color 0.91, luminance 0.94, texture 0.97, layout 0.95 |
| 0.820 | [`minimalism`](../style-packages/movements/minimalism/README.md) | [`slade-school-of-fine-art`](../style-packages/schools/slade-school-of-fine-art/README.md) | color 0.91, luminance 0.95, texture 0.96, layout 0.97 |

## 全量包签名清单

| 分类 / ID | 包摘要（差异锚点） | 关系签名 |
|---|---|---|
| `artists/agnes-martin` | 以极细网格、重复线条、低对比色带和安静留白构成极简绘画，强调手绘重复中的微小偏差与长时间观看。 | 已列出 |
| `artists/albrecht-durer` | 以精确轮廓、细密排线、结构化明暗和纸面印痕组织画面，并把体积与材质落实在线条密度和明暗秩序中。 | 已列出 |
| `artists/alphonse-mucha` | 以流动曲线、植物纹样、人物与边框的连续节奏、温暖纸色和装饰性平面组织画面；本包提取穆夏式视觉语法，不固定女性肖像、花卉、广告或文字。 | 已列出 |
| `artists/anna-ancher` | A northern interior-painting profile centered on changing daylight, quiet domestic tasks, simplified forms, and color relationships that make light the subject rather than a decorative effect. | 已列出 |
| `artists/artemisia-gentileschi` | 写实油画与大胆的肉身造型；人物以强烈对角线和近距离动作挤压画面，形成有力的叙事瞬间；深黑、血红、赭金、钴蓝与象牙白形成高对比巴洛克色组。 | 已列出 |
| `artists/berthe-morisot` | 以高明度色调、迅疾松动的笔触、开放的边缘和流动日光组织画面，让人物与环境在轻盈的色块中相互渗透。 | 已列出 |
| `artists/bridget-riley` | 以重复条带、曲线和黑白或有限色彩关系制造视觉振动，强调画面平面与观看者感知之间的主动关系。 | 已列出 |
| `artists/caravaggio` | Independent Caravaggio style package focused on 明暗对照、单一光源、普通人物与戏剧性空间; it requires new subjects and arrangements. | 已列出 |
| `artists/caspar-david-friedrich` | 以孤寂尺度、背向观看、清冷空气和远景层叠组织风景，让自然的精神重量超过具体叙事。 | 已列出 |
| `artists/claude-monet` | A reference-backed landscape painting profile focused on transient light, atmospheric color, broken touches, and the changing appearance of ordinary motifs rather than heavy contour or expressive impasto. | 已列出 |
| `artists/diego-rivera` | 以壁画式大尺度结构、清晰轮廓、平面色块和公共空间的叙事组织画面，同时保持用户主体开放。 | 已列出 |
| `artists/diego-velazquez` | A court and portrait painting profile built from controlled dark space, selective illumination, precise faces and fabrics, and lively broad passages that dissolve at the edges. | 已列出 |
| `artists/edgar-degas` | Independent Edgar Degas style package focused on 裁切视角、高机位、非对称构图与舞者动作; it requires new subjects and arrangements. | 已列出 |
| `artists/edouard-manet` | 以平直而有张力的色面、现代生活的截取感、清晰轮廓和不完全抛光的笔触打破传统画面秩序。 | 已列出 |
| `artists/edvard-munch` | A reference-backed expressionist painting profile focused on psychological color, contour that carries bodily tension, compressed space, and recurring organic or architectural rhythms without copying an iconic image. | 已列出 |
| `artists/edward-hopper` | 以现代城市和海岸生活中的简化建筑、孤立人物、强烈窗光与克制色彩构成悬置的日常场景，强调观看距离和心理空间。 | 已列出 |
| `artists/egon-schiele` | 干涩线描、扭曲人体和稀疏水彩色块；人物或物体以扭曲姿态、尖锐负形和不稳定边缘占据空白纸面；骨白、砖红、暗绿、烟灰和黑线形成裸露而克制的色组。 | 已列出 |
| `artists/el-greco` | Independent El Greco style package focused on 拉长形体、垂直升腾、冷色灵光与压缩空间; it requires new subjects and arrangements. | 已列出 |
| `artists/el-lissitzky` | 以几何构造、空间投影、斜向动力和工程化版式建立视觉秩序，适合抽象图形、建筑表面与信息结构。 | 已列出 |
| `artists/eugene-delacroix` | Independent Eugène Delacroix style package focused on 对角线运动、暖冷冲突、饱和色与自由笔触; it requires new subjects and arrangements. | 已列出 |
| `artists/francis-bacon` | 通过扭曲人物、封闭空间、强烈色块和肉身张力建立不安而具体的现代绘画语言 | 已列出 |
| `artists/francisco-de-zurbaran` | 静物与人物的雕塑性油画；孤立主体、安静的几何体和大面积暗背景制造修道院式静默；炭黑、灰白、赭褐、暗红和少量金黄形成克制色组。 | 已列出 |
| `artists/francisco-goya` | Independent Francisco Goya style package focused on 心理张力、暗色现实、粗粝笔触与不安静默; it requires new subjects and arrangements. | 已列出 |
| `artists/frida-kahlo` | 以正面肖像、私人象征、清晰轮廓和民俗色彩组织亲密而有心理张力的画面。 | 已列出 |
| `artists/georges-seurat` | A Neo-Impressionist painting profile built from disciplined optical color units, stable silhouettes, measured park-like space, and calm repeated social poses. | 已列出 |
| `artists/georgia-okeeffe` | 平滑渐变、放大花卉或骨骼形体与简洁背景；单一自然形体被放大到接近抽象，边缘清洁且画面留白充足；骨白、沙色、深红、灰蓝和干燥黑形成沙漠般色组。 | 已列出 |
| `artists/gerhard-richter` | 以照片绘画的柔焦、刮板拖拽和抽象色层在具象与非具象之间制造不确定的观看。 | 已列出 |
| `artists/giorgio-de-chirico` | 以空旷广场、长阴影、古典建筑、雕像与不合时宜的物体构成形而上绘画，强调静止空间中的悬置感与谜题感。 | 已列出 |
| `artists/giorgio-morandi` | 以克制的灰粉色调、低矮器物关系和近乎静止的空间节奏，观察日常形体之间的微妙差异。 | 已列出 |
| `artists/grant-wood` | Independent Grant Wood style package focused on 乡土几何、清晰垂直形、冷静中西部色调与细密描绘; it requires new subjects and arrangements. | 已列出 |
| `artists/gustav-klimt` | 金箔联想、平面装饰和局部写实身体结合；人物被装饰性平面、金色图案和垂直背景包围，身体关系被图案化；金黄、黑、象牙、深紫与孔雀蓝形成装饰性对比。 | 已列出 |
| `artists/gustave-courbet` | Independent Gustave Courbet style package focused on 厚重物质感、未理想化人物、土色现实与坚实地面; it requires new subjects and arrangements. | 已列出 |
| `artists/gustave-moreau` | 以象征性的线条、宝石般色彩、装饰性细节和梦境般的空间组织画面，让想象性保持开放。 | 已列出 |
| `artists/henri-matisse` | Independent Henri Matisse style package focused on 平面色块、装饰性空间、简化轮廓与大胆色彩; it requires new subjects and arrangements. | 已列出 |
| `artists/henri-rousseau` | 以平面化形体、清晰轮廓、装饰性植物层次和均匀光线构成天真而精确的空间。 | 已列出 |
| `artists/hilma-af-klint` | 以几何图式、螺旋、对称结构和富有精神象征意味的色彩组织抽象绘画，强调符号系统的秩序与柔性变化。 | 已列出 |
| `artists/ivan-aivazovsky` | 以海面、天空、航船和光线交汇构成浪漫主义海景，强调水面运动、空气透视、月光或夕照的单一光源和宏阔尺度。 | 已列出 |
| `artists/jan-van-eyck` | 细密油画、透明釉层和高精度细节；室内正面空间、镜面反射和精密小物共同构成静默的仪式感；深红、橄榄绿、木棕、蓝灰与珍珠白形成宝石般低亮色组。 | 已列出 |
| `artists/jean-auguste-dominique-ingres` | 以清晰而有弹性的轮廓、克制的明暗和理想化的形体秩序建立新古典主义的稳定视觉语言。 | 已列出 |
| `artists/jean-michel-basquiat` | 以粗粝线条、断裂形体、符号化标记和高张力色块组织画面，保留手工痕迹与城市现场感。 | 已列出 |
| `artists/jmw-turner` | An atmospheric landscape painting profile built from dissolving edges, vaporous layered paint, luminous weather, and directional spatial movement without reproducing a named marine or railway composition. | 已列出 |
| `artists/joan-miro` | Independent Joan Miró style package focused on 生物形态线条、留白、原色岛屿与轻盈非对称; it requires new subjects and arrangements. | 已列出 |
| `artists/joan-mitchell` | 以大面积留白、强烈而断续的笔触、滴落与擦拭痕迹，把可辨认的景观记忆转化为开放的抽象空间。 | 已列出 |
| `artists/johannes-vermeer` | An interior and cityscape painting profile built from controlled side light, quiet geometry, measured domestic detail, and soft optical transitions. | 已列出 |
| `artists/kathe-kollwitz` | 以黑白版画、炭笔线网、压缩构图和强烈明暗把普通形体转化为具有重量的视觉表达。 | 已列出 |
| `artists/katsushika-hokusai` | 以清晰刻线、平涂色块、受控套色和强烈的波形节奏组织画面；风格重点在图形化空间、装饰性负形与木版印刷的触感，不固定海浪、船只或任何特定地点。 | 已列出 |
| `artists/kazimir-malevich` | 以悬浮的几何形体、非对象化空间和极少的色彩关系，建立不依赖具体物件的纯粹秩序。 | 已列出 |
| `artists/leonardo-da-vinci` | Independent Leonardo da Vinci style package focused on 晕涂、观察性解剖、空气透视与自然研究; it requires new subjects and arrangements. | 已列出 |
| `artists/leonora-carrington` | 以梦境般的生物、炼金意象、细密轮廓和冷静而神秘的空间构成超现实绘画，强调多义形象与精细表面。 | 已列出 |
| `artists/louise-bourgeois` | 以有机与建筑性形体、压缩空间、粗粝表面和记忆感的结构张力组织画面。 | 已列出 |
| `artists/marc-chagall` | 以漂浮的人物关系、梦境般的空间错置和强烈但不均匀的色彩叙事，建立带有民间诗意的开放画面。 | 已列出 |
| `artists/mary-cassatt` | 印象派笔触与粉彩般的柔软边缘；亲密的室内关系、偏近的裁切和自然姿态构成日常生活片段；柔和粉、薄荷绿、奶油黄、灰蓝和肤色形成轻盈色组。 | 已列出 |
| `artists/mc-escher` | 以精密线刻、连续镶嵌、错视空间、反射对称与几何变形组织画面，保持版画般的清晰边缘和可解释的结构秩序。 | 已列出 |
| `artists/michelangelo-buonarroti` | Independent Michelangelo Buonarroti style package focused on 纪念性人体、雕塑式体积、复杂透视与强轮廓; it requires new subjects and arrangements. | 已列出 |
| `artists/moholy-nagy` | 以光作为材料，结合几何构成、透明叠层、机械运动感与高反差黑白结构，形成跨越绘画、摄影与设计的实验视觉语言。 | 已列出 |
| `artists/nicolas-de-stael` | 以厚重而清晰的色块、被压缩的空间和介于具象与抽象之间的形体，建立具有重量感的开放绘画语言。 | 已列出 |
| `artists/norman-rockwell` | 叙事性商业插画、清晰轮廓与细密生活道具；小型人物关系、清楚动作和可读道具组成带有幽默的叙事插画；暖红、奶油、深蓝、棕色和少量黄形成亲切印刷色组。 | 已列出 |
| `artists/pablo-picasso` | Independent Pablo Picasso style package focused on 分析性平面、多视点、结构化静物与几何重组; it requires new subjects and arrangements. | 已列出 |
| `artists/paul-cezanne` | A painting profile built from constructive color planes, compressed perspective, repeated directional brush marks, and objects that remain solid while viewpoints subtly disagree. | 已列出 |
| `artists/paul-gauguin` | A Synthetist painting profile built from flattened color fields, strong contour design, symbolic non-natural color, compressed spatial layers, and decorative rhythm. | 已列出 |
| `artists/paul-klee` | 以游移线条、半透明色块、符号化形体和轻盈的平面节奏组织画面，让抽象秩序保持手工痕迹与开放联想。 | 已列出 |
| `artists/peter-paul-rubens` | 以充满动势的斜向构图、肉身与布料的丰润体积、温暖高光和厚薄交错的油彩组织画面，保持主体开放。 | 已列出 |
| `artists/pierre-auguste-renoir` | Independent Pierre-Auguste Renoir style package focused on 明亮户外光、柔和肤色、破碎色点与社交氛围; it requires new subjects and arrangements. | 已列出 |
| `artists/pierre-bonnard` | 以亲密日常中的色彩震动、装饰性平面和不断变化的室内光线组织画面，让普通主体保留记忆般的温度。 | 已列出 |
| `artists/piet-mondrian` | 以网格秩序、非对称平衡和少量原色平面组织纯粹的绘画空间，强调结构关系而不是固定题材。 | 已列出 |
| `artists/pieter-bruegel-the-elder` | Independent Pieter Bruegel the Elder style package focused on 高视点全景、微小群像、季节劳动与乡土地景; it requires new subjects and arrangements. | 已列出 |
| `artists/raphael-sanzio` | Independent Raphael style package focused on 理想化人体、平衡群像、清晰轮廓与古典秩序; it requires new subjects and arrangements. | 已列出 |
| `artists/rembrandt` | A reference-backed baroque painting profile focused on directional light, psychological presence, warm dark grounds, layered flesh and cloth, and selective tactile paint rather than a generic brown filter. | 已列出 |
| `artists/rene-magritte` | 以冷静写实的日常物件、尺度错置、图像悖论与清晰轮廓制造陌生感。 | 已列出 |
| `artists/romare-bearden` | 纸张拼贴、绘画色块与手工边缘；人物和城市空间由切割平面、重叠形状和碎片化视线组成；深蓝、砖红、芥末黄、奶油和黑色形成爵士般撞色。 | 已列出 |
| `artists/salvador-dali` | 以精细写实表面、梦境逻辑、延展阴影和不稳定形体构成清醒而陌生的超现实画面。 | 已列出 |
| `artists/sandro-botticelli` | 蛋彩画式平面色层与精细线描；优雅的线性轮廓、平衡的神话人物群组和轻盈的风向线组织平面叙事；淡蓝、贝壳粉、草绿、金发黄与乳白形成清澈的早期文艺复兴色组。 | 已列出 |
| `artists/sofonisba-anguissola` | 以清晰而柔和的肖像塑造、敏锐的目光交流和克制的衣料细节呈现人物关系，让表情与手势承担叙事。 | 已列出 |
| `artists/sonia-delaunay` | 以同时性对比、圆弧节奏和色彩运动组织画面，让绘画、设计与织物之间形成连续的视觉韵律。 | 已列出 |
| `artists/tamara-de-lempicka` | 以装饰艺术时期的几何构形、金属般清晰的体积、冷峻优雅的人物和高对比色面组织现代肖像与静物。 | 已列出 |
| `artists/titian` | 以文艺复兴晚期威尼斯绘画的丰润色彩、温暖光泽与层叠油彩表面组织画面。它关注色彩如何承载体积、肌理和情绪，不规定人物、物体或地点。 | 已列出 |
| `artists/utagawa-hiroshige` | 以远近层叠、季节气候、留白与裁切式视角组织木版画画面，强调空气、节奏和自然形体的简洁秩序。 | 已列出 |
| `artists/vincent-van-gogh` | A post-impressionist painting profile built from observed directional strokes, high-chroma complementary color, thick material paint, and expressive motion in sky, vegetation, and ground without copying a named composition. | 已列出 |
| `artists/wassily-kandinsky` | An abstract painting profile built from geometric and lyrical marks, measured color tensions, layered planes, and compositional balance without narrative illustration. | 已列出 |
| `artists/yayoi-kusama` | 以重复、增殖、网状覆盖、软雕塑和镜面空间制造近乎无限的观看经验，并让单一视觉单位不断扩张。 | 已列出 |
| `artists/yves-klein` | 以国际克莱因蓝、单色表面、海绵质地和身体痕迹探索色彩作为空间与物质的艺术语言。 | 已列出 |
| `movements/abstract-expressionism` | 动作绘画、厚薄笔触和开放画布；大尺度画面由手势笔触和局部空白建立非中心构图；黑、赭红、钴蓝、乳白和橙黄形成高能量色层。 | 已列出 |
| `movements/aestheticism` | 以艺术整体性、感官表面、装饰性统一和克制的不对称关系组织图像、物件与空间。 | 已列出 |
| `movements/american-luminism` | 以稀疏的横向景观、克制的边缘、平静水面和精密大气透视捕捉冷静、清澈且近乎静止的自然光。 | 已列出 |
| `movements/art-brut` | 以未经学院规范驯化的线条、重复、密集痕迹和非标准材料感，保留直接、私人且不完美的视觉生成过程。 | 已列出 |
| `movements/art-deco` | Independent Art Deco style package focused on 阶梯几何、对称、金属色与现代奢华; it requires new subjects and arrangements. | 已列出 |
| `movements/art-informel` | 以反几何构成、偶发痕迹、材料厚度和松散手势拒绝整齐的形式秩序。 | 已列出 |
| `movements/art-nouveau` | Independent Art Nouveau style package focused on 鞭梢曲线、植物形态、平面装饰与柔和珠宝色; it requires new subjects and arrangements. | 已列出 |
| `movements/arte-povera` | 以非贵重材料、临时结构、自然变化、粗粝表面和材料之间的张力组织画面，强调物质过程而非装饰性完成度。 | 已列出 |
| `movements/arts-and-crafts` | 手工木作、织物、壁纸和建筑装饰；建筑、家具和图案共同形成可使用的整体，手工痕迹可见；苔绿、砖红、蜂蜜黄、深蓝和米白形成自然装饰色组。 | 已列出 |
| `movements/baroque` | Independent Baroque style package focused on 戏剧光线、对角线运动、深暗背景与材质丰富度; it requires new subjects and arrangements. | 已列出 |
| `movements/bohemian` | 以自由混搭、手工材质、旅行物件、自然色彩和不规则层次构成松弛而富有生活痕迹的视觉。 | 已列出 |
| `movements/brutalism` | 以裸露结构、厚重体块、粗粝材质、强烈比例和直接功能表达建立不修饰的建筑与平面视觉。 | 已列出 |
| `movements/byzantine-art` | 以正面秩序、金色或深色背景、稳定轮廓、象征性尺度和克制的平面层次建立超越日常空间的视觉庄严感。 | 已列出 |
| `movements/chinese-literati-ink-painting` | 以墨色浓淡、笔触速度、留白空间和含蓄的观看节奏组织画面；强调笔墨本身的气韵与主体之间的距离，不固定竹子、山水、亭台或卷轴形式。 | 已列出 |
| `movements/color-field-painting` | 以大面积、低调制的色面组织视觉空间、观看节奏和情绪，不依赖明确的中心叙事 | 已列出 |
| `movements/conceptual-art` | 现成物、文档式摄影和文字结构的视觉替代，但画面不出现可读文字；一个简单规则或观念决定物件排列，形式故意保持克制；白、黑、纸灰、红色标记和自然色形成概念性对比。 | 已列出 |
| `movements/constructivism` | 几何构成、印刷设计与工业材料感；对角线、圆弧、网格和机械结构构成强烈的平面空间；黑、白、红、黄和工业灰形成革命性几何色组。 | 已列出 |
| `movements/coquette` | 以蝴蝶结、柔和粉彩、细腻织物、轻盈装饰和浪漫细节构成精致但不固定人物身份的少女感视觉。 | 已列出 |
| `movements/cubism` | Independent Cubism style package focused on 多视点、切面、浅空间与结构化静物; it requires new subjects and arrangements. | 已列出 |
| `movements/dada` | 拼贴、现成物、照片碎片和粗糙排版痕迹；现成物、错位比例和拼贴版面打断传统构图秩序；黑白、广告红、酸黄、灰纸和工业蓝形成冲突色组。 | 已列出 |
| `movements/de-stijl` | Builds clarity through horizontal-vertical relations, rectangular color fields, black structural lines, and asymmetrical balance, treating composition as a system rather than a few colored shapes. | 已列出 |
| `movements/deconstructivist-architecture` | 以倾斜体块、断裂轴线、非中心构图、结构与表皮的紧张关系组织建筑空间；本包控制空间语言和材料表现，不固定博物馆、尖塔或任何具体建筑。 | 已列出 |
| `movements/expressionism` | Independent Expressionism style package focused on 情绪变形、尖锐轮廓、强烈色彩与心理空间; it requires new subjects and arrangements. | 已列出 |
| `movements/farmhouse-cottagecore` | 以乡村生活的自然材质、朴素器物、植物、织物和温暖日光构成实用而有季节感的空间视觉。 | 已列出 |
| `movements/fauvism` | 以任意色彩、强烈色块、自由笔触、简化形体和深色轮廓组织画面；本包提取野兽主义的色彩与笔触逻辑，不固定海港、桥梁、人物或南法风景。 | 已列出 |
| `movements/fluxus` | 以事件分数、日常材料、开放行动、反精致处理和跨媒介关系组织视觉任务，让普通动作成为可观察的构成规则，而不是固定故事或道具清单。 | 已列出 |
| `movements/futurism` | Independent Futurism style package focused on 速度、重复节奏、对角线力量、城市机械感; it requires new subjects and arrangements. | 已列出 |
| `movements/gothic` | 以垂直性、尖拱、深色材质、宗教象征和复杂装饰建立庄严、神秘且结构明确的历史视觉。 | 已列出 |
| `movements/graffiti` | 以手写笔触、喷漆边缘、叠写层次、城市表面和高能色块构成直接而有现场感的视觉语言。 | 已列出 |
| `movements/greek-archaic-period` | A transitional Greek visual language where patterned figures become more naturalistic, narrative pottery expands, and black-figure or red-figure contrast organizes bodies, animals, ornament, and mythic action. | 已列出 |
| `movements/greek-classical-period` | A measured Greek visual language of balanced composition, clear naturalistic bodies, calm agency, articulated drapery, and a disciplined relationship between movement, proportion, and civic ideals. | 已列出 |
| `movements/greek-geometric-period` | An early Greek visual system built from ordered registers, angular bodies, repeated signs, funerary procession, and a tightly controlled terracotta, black, and cream material language. | 已列出 |
| `movements/greek-hellenistic-period` | A late Greek visual language of energetic diagonals, torsion, emotional intensity, varied bodies, theatrical space, and contact between Greek and eastern Mediterranean traditions after the Macedonian expansion. | 已列出 |
| `movements/harlem-renaissance` | 绘画、海报、拼贴与舞台性构图结合；人物、音乐、城市街道和装饰平面共同形成文化自信的场景；深棕、金黄、孔雀蓝、朱红和黑色形成爵士般色组。 | 已列出 |
| `movements/impressionism` | Independent Impressionism style package focused on 瞬时光、破碎笔触、反射色与户外空气; it requires new subjects and arrangements. | 已列出 |
| `movements/international-typographic-style` | Independent International Typographic Style style package focused on 网格、无衬线秩序、非对称留白与清晰信息层级; it requires new subjects and arrangements. | 已列出 |
| `movements/italian-high-renaissance-raphaelesque` | A sixteenth-century Italian painting system built on careful drawing, proportioned figures, coherent space, calm narrative action, and controlled color; Raphael's School of Athens is one reference case, not a template. | 已列出 |
| `movements/japandi` | 融合日式克制与北欧功能主义，以自然材质、低饱和色彩、留白和简洁比例建立安静空间。 | 已列出 |
| `movements/kawaii` | 以圆润轮廓、简化表情、柔和或糖果色彩和亲和比例构成轻松可爱的视觉，不限定具体角色。 | 已列出 |
| `movements/land-art` | 土地、石头、泥、盐和现场干预共同构成；巨大自然场地中的人工线条、圆环或挖掘痕迹形成尺度关系；土红、岩灰、沙黄、天蓝和植被绿形成自然色组。 | 已列出 |
| `movements/lyrical-abstraction` | 以身体性的笔触、开放边界、流动色层和不规则节奏，让绘画过程成为画面结构的一部分。 | 已列出 |
| `movements/magic-realism` | 具象绘画、细节写实与一个超现实但克制的事件；日常空间保持真实，但一个不解释的异常物体改变心理重心；尘土色、灰绿、暗红、乳白和冷蓝形成平静而异样的色组。 | 已列出 |
| `movements/mannerism` | 精细线描、扭曲比例与人工化色彩；修长人体、复杂扭转和非自然空间让人物关系产生紧张感；酸黄、冷粉、青绿、灰紫和象牙白形成不稳定对比。 | 已列出 |
| `movements/memphis` | 以几何形体、明亮撞色、装饰性图案和不对称组合打破严肃功能主义，形成 playful 的平面空间。 | 已列出 |
| `movements/mexican-muralism` | 以公共尺度的整体构图、坚实轮廓、分层色块和壁面叙事秩序组织视觉信息，强调画面结构的可读性与公共空间感。 | 已列出 |
| `movements/mid-century-modern` | 以20世纪中叶的简洁家具、木材、流线形体、功能主义比例和明快但克制的色彩建立现代生活视觉。 | 已列出 |
| `movements/minimalism` | 工业几何体、硬边表面与极少装饰；少量基本形体占据宽阔空间，比例和间距成为主体；白、灰、黑、冷蓝和单一强调色形成低噪声色组。 | 已列出 |
| `movements/mughal-miniature-painting` | 以细密笔触、清晰轮廓、层叠空间、平面化色块与精确自然观察组织画面，保留纸本、矿物色和金色装饰的手工感。 | 已列出 |
| `movements/neo-dada` | 以现成物、拼贴、偶发动作与媒介混用打破艺术品和日常物之间的边界，保持反权威的实验感。 | 已列出 |
| `movements/neo-expressionism` | 以粗粝笔触、变形具象和强烈色块把情绪压力带回绘画表面，同时保留主体的冲突性。 | 已列出 |
| `movements/neoclassicism` | Independent Neoclassicism style package focused on 清晰轮廓、古典建筑、平衡几何与雕塑式人体; it requires new subjects and arrangements. | 已列出 |
| `movements/neue-sachlichkeit` | A Weimar-era visual language of matter-of-fact realism, hard-edged observation, social typology, and unsentimental attention to bodies, interiors, labor, and the consequences of modern life. | 已列出 |
| `movements/new-topographics` | A landscape-photography movement profile built around clear-eyed views of human-altered terrain, restrained composition, neutral description, and the tension between documentary evidence and aesthetic order. | 已列出 |
| `movements/nihonga` | 以纸、绢、矿物颜料、蛤粉与胶为材料基础，结合细线、平静留白、自然观察和层叠色面形成现代日本绘画语言。 | 已列出 |
| `movements/northern-renaissance` | 细密油画、透明釉层与超写实小物；室内细节、反射物和小尺度象征共同构成精密叙事；深红、墨绿、金黄、木棕和铅白形成细密色组。 | 已列出 |
| `movements/op-art` | 硬边几何、重复图案和视错觉结构；重复线条、网格和波纹制造视觉震动，画面保持平面；黑白为主，辅以单一红或蓝强调色。 | 已列出 |
| `movements/orientalism` | 研究十九世纪欧洲艺术中的东方想象及其事实与幻想的交错，提取装饰性空间、暖土色、冷色阴影和材质细节，同时明确反对把族群、地点或异国情节写成默认主体。 | 已列出 |
| `movements/orphism` | 以棱镜色面、圆弧节奏和同时对比研究光与色的运动感，不依赖可识别的具象主体。 | 已列出 |
| `movements/photorealism` | 精确绘画或摄影式图像，边缘和细节高度可控；照片式裁切和日常对象被精确还原，画面冷静而无戏剧性；中性灰、真实肤色、车漆色和玻璃反光组成观察性色组。 | 已列出 |
| `movements/pictorialism` | 以摄影的柔焦、纹理纸面、手工印相和朦胧的光线表达摄影的绘画性，同时保留摄影构图与暗房过程的可观察线索。 | 已列出 |
| `movements/pointillism` | 以独立色点、光学混色、局部色彩并置和有节奏的点状笔触构成可辨识的绘画表面。 | 已列出 |
| `movements/pop-art` | 丝网印刷、硬边平涂、重复和商业图像语法；日常商品、广告式裁切和重复图像形成平面冲击；正红、亮黄、宝蓝、黑和纸白形成高纯度印刷色组。 | 已列出 |
| `movements/post-impressionism` | Independent Post-Impressionism style package focused on 结构化色块、主观色彩、稳定形体与可见笔触; it requires new subjects and arrangements. | 已列出 |
| `movements/pre-raphaelites` | 细密绘画、植物观察和中世纪式装饰；清晰前景植物、细密人物和装饰性叙事形成高密度平面；宝石绿、深红、蓝、金黄和乳白形成明亮精细色组。 | 已列出 |
| `movements/precisionism` | 几何化具象、清晰边缘与简化体积；工厂、仓库和桥梁被简化为清楚的几何体，人物很少；白、灰、铁蓝、砖红和黄褐形成工业色组。 | 已列出 |
| `movements/rayonism` | 以相交射线、透明色带、碎裂平面和方向性运动组织非具象画面，让光线关系取代物体轮廓成为构图骨架。 | 已列出 |
| `movements/realism` | Independent Realism style package focused on 普通劳动、直接观察、非理想化人物与土色重量; it requires new subjects and arrangements. | 已列出 |
| `movements/renaissance` | 蛋彩或油画结合古典素描与清晰轮廓；稳定的人体比例、清楚透视和金字塔式人物关系建立人文秩序；赭金、群青、朱红、石灰白和自然绿形成平衡色组。 | 已列出 |
| `movements/rococo` | Independent Rococo style package focused on 轻盈花园、粉彩、非对称姿态与精致装饰; it requires new subjects and arrangements. | 已列出 |
| `movements/romanesque-art` | 以厚重结构、正面叙事秩序、简化比例和矿物色彩建立坚实而清晰的中世纪视觉语言。 | 已列出 |
| `movements/romanticism` | Independent Romanticism style package focused on 崇高景观、天气、情绪尺度与暖冷光线; it requires new subjects and arrangements. | 已列出 |
| `movements/shabby-chic` | 以褪色表面、旧家具、柔和粉彩、手工痕迹和轻微磨损建立温柔而不完美的居家审美。 | 已列出 |
| `movements/situationist-international` | 以城市漂移、断裂地图、拼贴文本和对消费空间的重新编排，制造开放而批判性的视觉场景。 | 已列出 |
| `movements/socialist-realism` | 具象绘画、清楚轮廓和公共叙事构图；人物群体、劳动动作和清楚背景形成可读的公共场景；红、赭土、天蓝、暖灰和肤色形成正面但不霓虹的色组。 | 已列出 |
| `movements/steampunk` | 以维多利亚时代机械想象、黄铜齿轮、蒸汽装置、皮革和复古工业结构构成可解释的幻想设计。 | 已列出 |
| `movements/suprematism` | 纯几何抽象与硬边平涂；基本几何形体漂浮于开放底面，重力和比例被悬置；白、黑、红、蓝和黄形成纯净色面。 | 已列出 |
| `movements/surrealism` | Independent Surrealism style package focused on 梦境逻辑、日常错位、清晰质感与非理性连接; it requires new subjects and arrangements. | 已列出 |
| `movements/symbolism` | 平面化绘画、梦境意象与装饰性轮廓；现实场景被一两个心理象征物打断，构图宁静而不解释；深蓝、紫黑、月白、暗红和金黄形成梦境色组。 | 已列出 |
| `movements/synthwave` | 以复古电子音乐文化、霓虹地平线、紫蓝渐变、网格透视和强烈夜色对比建立合成未来视觉。 | 已列出 |
| `movements/tenebrism` | 以大面积暗部包围局部强光、深色背景和戏剧性明暗分割建立集中而有体积感的画面秩序。 | 已列出 |
| `movements/tonalism` | 以相近色阶、柔和空气和被雾化的远近关系建立低声部画面，而不是依赖鲜艳颜色或明确轮廓。 | 已列出 |
| `movements/ukiyo-e` | 一种以多色木版套印、清晰轮廓、装饰性平面、截取式构图和日常城市题材闻名的视觉传统；本包提取版画组织方法，不固定桥梁、灯笼或日本街景。 | 已列出 |
| `movements/utilitarian` | 以功能优先、耐用材料、清楚标识、结构诚实和克制装饰建立直接、可靠、可复用的设计视觉。 | 已列出 |
| `movements/vaporwave` | 以消费媒介怀旧、低清数字质感、粉紫青色调、古典雕像隐喻和错位排版构成网络亚文化视觉。 | 已列出 |
| `movements/victorian` | 以19世纪装饰秩序、繁复纹样、深色木材、织物层次和结构化室内细节形成历史感视觉。 | 已列出 |
| `movements/vienna-secession` | 以平面装饰、几何秩序、象征性图形和建筑—平面—工艺的整体关系组织画面。 | 已列出 |
| `movements/vorticism` | 以硬边折线、机械时代的动势、强烈色面和向中心压缩的结构，制造短促而有能量的现代主义画面。 | 已列出 |
| `schools/academie-julian` | 以巴黎私人工作室式教学、持续写生、炭笔人体习作和师生围绕画架交流为核心，呈现开放的职业化艺术训练氛围。 | 已列出 |
| `schools/academy-of-fine-arts-vienna` | 以观察、比例、结构素描、受控明暗和完成度优先的学院训练组织画面，强调从观察到完成的稳定方法。 | 已列出 |
| `schools/artcenter` | 以清晰的设计问题、专业化视觉沟通、精确的形式控制和可交付的呈现质量组织图像，不限定具体产品或行业对象。 | 已列出 |
| `schools/bauhaus` | Emphasizes geometric order, basic forms, primary-color relationships, functional structure, and negative space across graphic, spatial, product, and abstract compositions without copying a specific design. | 已列出 |
| `schools/black-mountain-college` | 以实践、协作、实验和跨媒介学习为核心的进步艺术教育传统，强调开放过程而非固定样式。 | 已列出 |
| `schools/california-college-of-the-arts` | 以湾区开放工作室、艺术与设计协作、建筑模型和可持续材料实验组织视觉学习。 | 已列出 |
| `schools/california-institute-of-the-arts` | 以跨媒介、批判思考、实验制作和展览语境之间的往返，形成开放而过程导向的当代艺术提案。 | 已列出 |
| `schools/central-saint-martins` | 以跨媒介实验、研究驱动的视觉沟通和材料工作坊把设计当作思考与制作共同推进的过程。 | 已列出 |
| `schools/cranbrook-academy` | 以驻校导师、工作室实践和跨学科材料实验为核心的设计教育传统。 | 已列出 |
| `schools/design-academy-eindhoven` | 以材料实验、批判性问题意识、社会语境和可讨论的原型结构组织设计图像。 | 已列出 |
| `schools/ecal` | 以跨学科、研究驱动和专业制作把摄影、平面、产品与数字媒介放在同一实验场中。 | 已列出 |
| `schools/glasgow-school-of-art` | 以建筑线性结构、装饰性自然形态和工艺细节共同组织视觉空间，强调结构与装饰之间的张力。 | 已列出 |
| `schools/new-bauhaus` | Independent New Bauhaus style package focused on 基础几何、实验构成、材料感与形式功能统一; it requires new subjects and arrangements. | 已列出 |
| `schools/paris-beaux-arts` | 以工作室观察、经典比例、材料训练和历史连续性建立学院派的基础方法。 | 已列出 |
| `schools/parsons-school-of-design` | 以城市语境、设计方法、对象研究和可执行的过程图谱组织视觉方案。 | 已列出 |
| `schools/risd` | 以材料实践、问题意识、批判思考和跨学科制作共同推动设计学习。 | 已列出 |
| `schools/royal-academy-schools` | 以长期工作室实践、写生训练、材料研究和个人视觉语言发展组织创作过程，强调训练方法而非固定画面题材。 | 已列出 |
| `schools/royal-college-of-art` | 以研究驱动、跨学科、材料实验和设计实践共同推动视觉方案，重视从问题到原型的转换过程。 | 已列出 |
| `schools/royal-danish-academy` | 以建筑、设计和材料研究之间的协作方法，强调结构清晰、环境责任与可验证的制作过程。 | 已列出 |
| `schools/school-of-the-art-institute-of-chicago` | 以跨学科研究、过程公开和展览语境中的实验性，连接绘画、物件、影像、空间与批评性编辑。 | 已列出 |
| `schools/school-of-visual-arts` | 以跨媒介实验、清晰的概念框架和面向展示的视觉叙事，组织平面、影像、物件与空间之间的关系。 | 已列出 |
| `schools/slade-school-of-fine-art` | 以开放的实验媒介、工作室研究、版画与雕塑实践建立跨学科的艺术教育方法。 | 已列出 |
| `schools/ulm-school` | Independent Ulm School style package focused on 功能主义、系统化网格、信息清晰与中性材料; it requires new subjects and arrangements. | 已列出 |
| `schools/yale-school-of-art` | 以研究、批判讨论、媒介专注和高度个人化的工作室实践形成当代学院气质。 | 已列出 |

## 审查准则

- 艺术家包按个人的媒介处理、构图、边缘、色彩和题材组织区分；不因共享时代或流派而合并。
- 流派包写跨作者共享的历史视觉语言；相邻流派需落到笔触、光线、空间、媒介或表面处理的差别。
- 学院包呈现机构的教学和工作方法；不把校名变成通用教室滤镜，也不让不同学院只靠相似画架场景区分。
- 图像候选分数需要结合实际内容看。明确不同的包保持独立并保留复核记录；语义上易混淆的包应继续调整 Prompt、README 和代表图。
