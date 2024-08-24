mkdir test-project-figma-main
touch test-project-figma-main/filefigma.figma
mkdir test-sources
mkdir test-sources/design
touch test-sources/test1.txt
echo "# Front-end Style Guide

## Layout

The designs were created to the following widths:

- Mobile: 375px
- Desktop: 1440px

> 💡 These are just the design sizes. Ensure content is responsive and meets WCAG requirements by testing the full range of screen sizes from 320px to large screens.

## Colors

### Primary

- Yellow: hsl(47, 88%, 63%)

### Neutral

- White: hsl(0, 0%, 100%)
- Grey: hsl(0, 0%, 50%)
- Black: hsl(0, 0%, 7%)

## Typography

### Body Copy

- Font size (paragraph): 16px

### Font

- Family: [Figtree](https://fonts.google.com/specimen/Figtree)
- Weights: 500, 800

> 💎 This is a free+ challenge. So, if you want to see all the design details and practice working with professional tools like Figma, you can download the design file from where you downloaded the starter code.
" > test-sources/style-guide.md
touch test-sources/README-template.md
echo "<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"> <!-- displays site properly based on user's device -->

  <link rel=\"icon\" type=\"image/png\" sizes=\"32x32\" href=\"./assets/images/favicon-32x32.png\">

  <style>
    @import url('https://fonts.googleapis.com/css2?family=Figtree:ital,wght@0,300..900;1,300..900&display=swap');
  </style>

  <title>Frontend Mentor | Blog preview card</title>

</head>
<body class=\"bg-primary font-figtree\">

  <main class=\"w-full h-screen flex justify-center items-center\">

    <!-- ombra custom: shadow-[{color}_{x_axis}px_{y_axis}px_{solidness}px_0px] -->

    <div class=\"bg-white w-[327px] md:w-[384px] p-6 rounded-2xl border border-black shadow-[black_8px_8px_0px_0px]\">
      <img class=\"rounded-xl\" src=\"./assets/images/illustration-article.svg\" alt=\"\">

      <div class=\"my-6 flex flex-col gap-4\">
        <div class=\"text-xs md:text-sm w-fit px-3 py-1 font-extrabold bg-primary rounded-md\">Learning</div>

        <p class=\"font-medium text-xs md:text-sm\">Published 21 Dec 2023</p>

        <h1 class=\"font-extrabold text-xl md:text-2xl active:text-primary active:cursor-pointer\">HTML & CSS foundations</h1>

        <p class=\"text-sm md:text-base text-grey\">These languages are the backbone of every website, defining structure, content, and presentation.</p>
      </div>

      <div class=\"flex gap-3 items-center\">
        <img class=\"w-8 aspect-square\" src=\"./assets/images/image-avatar.webp\" alt=\"\">

        <span class=\"font-extrabold text-sm\">Greg Hooper</span>
      </div>
    </div>

  </main>

</body>
</html>" > test-sources/index.html


cd ../..

rm -rf projects/test-project
