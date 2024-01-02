/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    colors:{
      'zenno-orange':'rgba(226, 94, 62, 1)',
      'zenno-white':'rgba(255, 255, 255, 1)',
      'zenno-black':'rgba(0, 0, 0, 1)',
    },
    extend: {},
  },
  plugins: [],
}

