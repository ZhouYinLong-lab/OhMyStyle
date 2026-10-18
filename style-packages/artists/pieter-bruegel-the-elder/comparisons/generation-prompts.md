# Prompts and visual review

The provider-neutral compiler jobs are included as `legacy-job.json` and `direction-job.json`. These are the image-generation prompts used for the paired probe.

## Legacy package

> Horizontal 16:9 wide elevated-view oil painting on wood, clearly hand-painted with matte paint and visible brushwork, not a photo. Show a present-day open public park with rolling hills and one winding path. Preserve exactly these requested subjects and actions: in the foreground, one cyclist repairing a bicycle; in the middle distance, exactly two friends unfolding a map; far away, exactly one person walking exactly one dog. Keep all four human figures and one dog, with no other people. Arrange this as a broad panoramic landscape where terrain occupies most of the image and the three activities appear at separate scales as natural details within it; let the path be part of the scenery, without making it a strong narrative connector. Use earthy greens and ochres, cool distant hills, naturalistic but simplified small figures, high viewpoint, crisp local details, and a balanced panorama. No farming, peasants, village, winter, castle, text, logo, watermark, or copied painting composition.

## New direction image

> Make a compositional edit to the legacy landscape for an experimental narrative direction. Preserve exactly the four people, one dog, one bicycle, all three activities, the public park, and horizontal 16:9 view. Do not add, remove or change any action. Rearrange only for a clear three-stage reading order: keep the cyclist repairing the bike large in the lower-left foreground; put the two friends with their map at a distinct middle-distance bend; put the single dog walker and dog at the far end. Make one continuous S-shaped park path visibly pass beside these three clusters in that order, so the path leads the eye from near to far. Reduce figure scale gradually along the route and use clear silhouettes to keep each activity distinguishable. Let the terrain remain one continuous landscape, and keep small naturalistic painted details subordinate to the three activity stations. Retain matte hand-painted Northern Renaissance oil-on-panel treatment and earthy park colors. No other people, dogs, activities, landmarks, text, logos, watermark, or copied arrangement from a named painting.

## Review

- **Held close:** both samples have the same scene, counts, three distinct activities, path, palette family, high viewpoint, and wide framing. The direction image is an image-to-image edit of the legacy sample, so it is controlled for scene but is not an independent generation.
- **Visible distinction:** the direction strengthens one S-shaped route and positions the three activity clusters more clearly along its near-to-far course. The legacy view distributes attention more evenly through the park.
- **Remaining issue:** the legacy image already contains a winding path that links the groups, so the difference is one of emphasis and reading order rather than an entirely new composition. Fine naturalistic detail also remains stronger than intended.
- **Status:** the sequence is visible in this single probe, but the image alone does not establish repeatability across subjects. Keep the direction and rule-level review experimental.

These are anonymous generated demonstrations, not reproductions of *The Harvesters* or another Bruegel work.
