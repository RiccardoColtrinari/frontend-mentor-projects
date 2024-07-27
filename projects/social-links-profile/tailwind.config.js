/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}", "index.html"],
  theme: {
    extend: {
      fontFamily: {
        'inter': ["Inter"]
      },
      colors: {
        'white': 'hsl(0, 0%, 100%)',
        'green': 'hsl(75, 94%, 57%)',
        'grey-700': 'hsl(0, 0%, 20%)',
        'grey-800': 'hsl(0, 0%, 12%)',
        'grey-900': 'hsl(0, 0%, 8%)',
      }
    },
  },
  plugins: [],
}