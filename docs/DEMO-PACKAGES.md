# Demo Package Set

The repository now includes one intentionally small package for each supported
direction:

| Direction | Demo | Primary focus |
| --- | --- | --- |
| Artist | [Anna Ancher](../style-packages/artists/anna-ancher/) | Northern light, domestic interiors, restrained color planes |
| Artist | [Claude Monet](../style-packages/artists/claude-monet/) | Transient outdoor light, broken adjacent color, weather, soft distant edges |
| Artist | [Edvard Munch](../style-packages/artists/edvard-munch/) | Emotional color, compressed space, undulating contour, psychological atmosphere |
| Artist | [J. M. W. Turner](../style-packages/artists/jmw-turner/) | Dissolving weather, luminous atmosphere, diagonal motion, lost-and-found edges |
| Artist | [Johannes Vermeer](../style-packages/artists/johannes-vermeer/) | Controlled side light, quiet geometry, domestic action, material transitions |
| Artist | [Paul Cézanne](../style-packages/artists/paul-cezanne/) | Constructive color planes, multiple-viewpoint tension, structural brush marks |
| Artist | [Rembrandt](../style-packages/artists/rembrandt/) | Warm dark ground, selective illumination, open shadow, tactile material focus |
| Artist | [Vincent van Gogh](../style-packages/artists/vincent-van-gogh/) | Directional impasto, complementary color pressure, expressive contour rhythm |
| Artist | [Wassily Kandinsky](../style-packages/artists/wassily-kandinsky/) | Abstract geometry, line rhythm, color weight, asymmetrical painted balance |
| Artist | [Diego Velázquez](../style-packages/artists/diego-velazquez/) | Selective baroque light, dark architectural field, social gaze, lost edges |
| Artist | [Georges Seurat](../style-packages/artists/georges-seurat/) | Optical color units, measured silhouettes, horizontal bands, still public rhythm |
| Artist | [Paul Gauguin](../style-packages/artists/paul-gauguin/) | Symbolic color fields, dark contour, compressed layers, decorative flatness |
| Photographer | [Masahisa Fukase](../style-packages/photographers/masahisa-fukase/) | Serial autobiography, intimacy, recurring motifs, psychological distance |
| Photographer | [Alfred Stieglitz](../style-packages/photographers/alfred-stieglitz/) | Authored geometry, layered planes, crop, weather, photogravure tonal structure |
| Photographer | [Eadweard Muybridge](../style-packages/photographers/eadweard-muybridge/) | Fixed camera, sequential phases, measurement grid, motion as evidence |
| Photographer | [Eugène Atget](../style-packages/photographers/eugene-atget/) | Neutral urban record, frontal space, quiet absence, archival tonal restraint |
| Photographer | [Julia Margaret Cameron](../style-packages/photographers/julia-margaret-cameron/) | Soft wet-plate focus, intimate pose, tonal atmosphere, expressive face |
| Photographer | [Lewis Hine](../style-packages/photographers/lewis-hine/) | Social evidence, direct context, human-machine scale, dignified observation |
| Photographer | [Nadar](../style-packages/photographers/nadar/) | Sculptural studio pose, plain ground, soft directional light, early print tone |
| Photographer | [Roger Fenton](../style-packages/photographers/roger-fenton/) | Restrained field documentary, aftermath evidence, deliberate terrain composition |
| Photographer | [Étienne-Jules Marey](../style-packages/photographers/etienne-jules-marey/) | Chronophotographic sequence, analytical traces, fixed ground, motion as evidence |
| Movement | [Neue Sachlichkeit](../style-packages/movements/neue-sachlichkeit/) | Matter-of-fact realism, social typology, precise surfaces |
| Movement | [Italian High Renaissance](../style-packages/movements/italian-high-renaissance-raphaelesque/) | Drawing, proportion, clear space, calm narrative action, controlled color |
| School / exhibition network | [New Topographics](../style-packages/schools/new-topographics/) | Clear-eyed views of human-altered landscape |
| Technique | [Gum Bichromate](../style-packages/techniques/gum-bichromate/) | Pigment, paper, contact exposure, layered hand control |
| Game art | [ZX Spectrum Attribute Pixel Art](../style-packages/game-art/zx-spectrum-attribute-pixel/) | 256×192 raster, 8×8 attribute cells, compact palette, controlled color clash |
| Game art | [RPG Maker Pixel Art](../style-packages/game-art/rpg-maker-pixel-art/) | Tile-based 2D scenes, compact sprites, nearest-neighbor edges, layered environments, optional warm-cool lighting |
| Preset | [Quiet Documentary](../styles/quiet-documentary/) | Original available-light photography preset |
| Preset | [High-Chroma Color Pairing](../style-packages/presets/high-chroma-color-pairing/) | Subject-neutral 撞色 system with high-chroma pairs, counter-grounds, and area-ratio checks |

The executable workflow for compiling generation jobs, selecting declared
references, evaluating renders, and recording local runs is documented in the
[Executable Style Package Workflow](EXECUTABLE-WORKFLOW.md).

## Ancient Greek chronology

The Ancient Greek direction is split into four period packages so that
chronology, material, anatomy, and narrative behavior can be evaluated
independently. See the [full expansion note](ANCIENT-GREEK-EXPANSION.md).

| Period | Demo | Primary focus |
| --- | --- | --- |
| Geometric | [Greek Geometric Period](../style-packages/movements/greek-geometric-period/) | Registers, angular signs, terracotta, repeated motifs |
| Archaic | [Greek Archaic Period](../style-packages/movements/greek-archaic-period/) | Contour narrative, ceramic fields, patterned naturalism |
| Classical | [Greek Classical Period](../style-packages/movements/greek-classical-period/) | Proportion, balance, measured weight shift, lucid space |
| Hellenistic | [Greek Hellenistic Period](../style-packages/movements/greek-hellenistic-period/) | Torsion, diagonal force, pathos, varied bodies |

These packages intentionally keep external works link-only. The reference
manifest records the source and rights status, while the anonymous prompt uses
observable traits instead of inserting the artist, photographer, or movement
name into the generation prompt. This gives the runtime a way to test whether
the structured package itself can reproduce the signature.

Validate the five new package directories with:

```bash
python3 tools/validate-package.py style-packages
python3 tools/validate-package.py styles/quiet-documentary
```
