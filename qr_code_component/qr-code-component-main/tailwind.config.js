/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}", "./index.html"],
  theme: {
    colors: {
      transparent: 'transparent',
      current: 'currentColor',
      'white': 'hsl(0, 0%, 100%)',
      'light-grey': 'hsl(212, 45%, 89%)',
      'grayish-blue': 'hsl(220, 15%, 55%)',
      'dark-blue': 'hsl(218, 44%, 22%)'
    },
    extend: {},
  },
  plugins: [],
}