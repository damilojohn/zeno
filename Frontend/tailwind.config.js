/** @type {import('tailwindcss').Config} */
export default {
  // content: ['./index.html', './src/*/.{js,ts,jsx,tsx}'],
  // content: ['./pages/**/*.{html,js}', './components/**/*.{html,js}'],
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      /* All colors used app-wide */
      colors: {
        'zenno-orange': 'rgba(226, 94, 62, 1)',
        'zenno-white': 'rgba(255, 255, 255, 1)',
        'zenno-black': 'rgba(0, 0, 0, 1)',
        'zenno-lblack': '#00000082',
        'zenno-2black': 'rgba(0, 0, 0, 0.70)',
        'zenno-1white': ' #FFF',
        'zenno-clear': ' rgba(255, 255, 255, 0.70)',
        'zenno-3black': '#000',
        'zenno-4black': 'rgba(0, 0, 0, 0.80)',
        'zenno-mwhite': '#F9FAFB',
        'zenno-aboutw': '#FFFCF6;',
        'zenno-aboutb': '#000000',
        'zenno-aboutb2': 'rgba(0, 0, 0, 0.60)',
      },
      fontSize: {},
      fontFamily: {},
      borderRadius: {
        sharp: '0',
        smooth: '0.5rem',
        rounded: '1rem',
        pill: '99999px',
      },

      fontWeight: {
        hairline: '100',
        thin: '200',
        light: '300',
        normal: '400',
        medium: '500',
        semibold: '600',
        bold: '700',
        extrabold: '800',
        black: '900',
      },
      /* All common box shadows */
      boxShadow: {
        custom: '0px 4px 0px 0px #141414',
        xs: '0px 2px 5px 0px rgba(103, 110, 118, 0.08), 0px 1px 1px 0px rgba(0, 0, 0, 0.12)',
        md: '0px 1px 1px 0px rgba(4, 101, 123, 0.12), 0px 0px 0px 1px rgba(4, 101, 123, 0.16), 0px 2px 5px 0px rgba(4, 101, 123, 0.08), 0px 2px 5px 0px rgba(103, 110, 118, 0.08)',
        lg: ' 0px 15px 35px 0px rgba(103, 110, 118, 0.08), 0px 5px 15px 0px rgba(0, 0, 0, 0.12)',
        hoverPrimary:
          '0px 1px 1px 0px rgba(4, 101, 123, 0.12), 0px 0px 0px 1px rgba(4, 101, 123, 0.64), 0px 2px 5px 0px rgba(4, 101, 123, 0.08)',
        hoverSecondary:
          '0px 1px 1px 0px rgba(4, 101, 123, 0.12), 0px 0px 0px 1px rgba(3, 72, 87, 0.24), 0px 2px 5px 0px rgba(3, 72, 87, 0.08)',
        hoverError:
          '0px 1px 1px 0px rgba(0, 0, 0, 0.12), 0px 0px 0px 2px rgba(243, 65, 65, 0.40), 0px 2px 5px 0px rgba(243, 65, 65, 0.08)',
        hoverWarning:
          ' 0px 1px 1px 0px rgba(0, 0, 0, 0.12), 0px 0px 0px 2px rgba(233, 162, 59, 0.40), 0px 2px 5px 0px rgba(233, 162, 59, 0.08)',
        hoverSuccess:
          '0px 1px 1px 0px rgba(0, 0, 0, 0.12), 0px 0px 0px 2px rgba(83, 180, 131, 0.40), 0px 2px 5px 0px rgba(83, 180, 131, 0.08)',
        focusPrimary:
          '0px 1px 1px 0px rgba(4, 101, 123, 0.12), 0px 0px 0px 1px rgba(4, 101, 123, 0.64), 0px 2px 5px 0px rgba(4, 101, 123, 0.08), 0px 0px 0px 4px rgba(4, 101, 123, 0.16)',
        focusSecondary:
          '0px 1px 1px 0px rgba(0, 0, 0, 0.12), 0px 0px 0px 1px rgba(4, 101, 123, 0.16), 0px 2px 5px 0px rgba(4, 101, 123, 0.08), 0px 0px 0px 4px rgba(132, 229, 251, 0.16)',
        focusError:
          ' 0px 1px 1px 0px rgba(0, 0, 0, 0.12), 0px 0px 0px 1px rgba(243, 65, 65, 0.16), 0px 2px 5px 0px rgba(103, 110, 118, 0.08), 0px 0px 0px 4px rgba(243, 65, 65, 0.16)',
        focusWarning:
          '0px 1px 1px 0px rgba(0, 0, 0, 0.12), 0px 0px 0px 1px rgba(233, 162, 59, 0.16), 0px 2px 5px 0px rgba(103, 110, 118, 0.08), 0px 0px 0px 4px rgba(233, 162, 59, 0.16)',
        focusSuccess:
          '0px 1px 1px 0px rgba(0, 0, 0, 0.12), 0px 0px 0px 1px rgba(83, 180, 131, 0.16), 0px 2px 5px 0px rgba(103, 110, 118, 0.08), 0px 0px 0px 4px rgba(83, 180, 131, 0.16)',
      },
      /* Animations */
      keyframes: {
        rotate: {
          '0%': {
            transform: 'rotate(0deg)',
          },
          '100%': {
            transform: 'rotate(360deg)',
          },
        },
      },
      animation: {
        rotate: 'rotate 1s ease infinite',
      },
    },
    spacing: {
      space0: '0rem',
      space025: '0.125rem',
      space050: '0.25rem	',
      space075: '0.375rem	',
      space100: '0.5rem	',
      space150: '0.75rem',
      space200: '1rem',
      space250: '1.25rem	',
      space300: '1.5rem',
      space400: '2rem',
      space500: '2.5rem	',
      space600: '3rem',
      space800: '4rem',
      space1000: '5rem',
    },
    screens: {
      '2xl': {max: '1535px'},
      // => @media (max-width: 1535px) { ... }

      xl: {max: '1279px'},
      // => @media (max-width: 1279px) { ... }

      lg: {max: '1023px'},
      // => @media (max-width: 1023px) { ... }

      md: {max: '767px'},
      // => @media (max-width: 767px) { ... }

      sm: {max: '639px'},
      // => @media (max-width: 639px) { ... }
    },
  },
  plugins: [],
};
