# Demo Package Set

The repository now includes one intentionally small package for each supported
direction:

| Direction | Demo | Primary focus |
| --- | --- | --- |
| Artist | [Anna Ancher](../style-packages/artists/anna-ancher/) | Northern light, domestic interiors, restrained color planes |
| Photographer | [Masahisa Fukase](../style-packages/photographers/masahisa-fukase/) | Serial autobiography, intimacy, recurring motifs, psychological distance |
| Movement | [Neue Sachlichkeit](../style-packages/movements/neue-sachlichkeit/) | Matter-of-fact realism, social typology, precise surfaces |
| Movement | [Italian High Renaissance](../style-packages/movements/italian-high-renaissance-raphaelesque/) | Drawing, proportion, clear space, calm narrative action, controlled color |
| School / exhibition network | [New Topographics](../style-packages/schools/new-topographics/) | Clear-eyed views of human-altered landscape |
| Technique | [Gum Bichromate](../style-packages/techniques/gum-bichromate/) | Pigment, paper, contact exposure, layered hand control |
| Game art | [ZX Spectrum Attribute Pixel Art](../style-packages/game-art/zx-spectrum-attribute-pixel/) | 256×192 raster, 8×8 attribute cells, compact palette, controlled color clash |
| Preset | [Quiet Documentary](../styles/quiet-documentary/) | Original available-light photography preset |

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
