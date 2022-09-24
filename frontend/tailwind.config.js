/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./public/index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        'corme':'Cormorant Garamond',
        'rale':'Raleway'
      }
    },
  },
  plugins: [],
}