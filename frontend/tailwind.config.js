/** @type {import('tailwindcss').Config} */


const colors = {
  primary:{
      100:"#282C30", //MAIN BG
      200:"#2F333A", //CONTENT BG CENTER
      300:"#F7F7F7", //TEXT
      400:"#2E2E2E", //input fields
  },
  red:{
    100:#fc2f70,
  },
  borders:{
      green:"#86c232",
      purple:"#C778DD",
      grey:"#D9D9D9"
  },
  sections:{
      about_me:"#C778DD", //3% OPACITY NEEDED,
      skills:"",
      what_i_do:"#46005C", //3% OPACITY NEEDED,
      achievements:"#1A1A1A",
      projects:"#1A1A1A",
      contact_me:"#1A1A1A"
  },
  buttons:{
      success:"#407C0A"
  },
  text:{
      purple:"#ce7fe4",
      green: "#48894A",
      yellow:"#C0B321",
      red: "#BE1C1C",
      blue:"#0A84FF"
  },
  table:{
    dark:"#1A1A1A",
    medium:"#2A2A2A",
    light:""
  },
  messages:{
    error:"#A34343",
    success:"#43A348"
  }
}

export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors,
      fontFamily: {
        roboto: ['Roboto', 'sans-serif'],
        pixelify: ['Pixelify', 'sans-serif'],
      },
      keyframes: {
        'star-movement-bottom': {
          '0%':   { transform: 'translate(0%, 0%)', opacity: '1' },
          '100%': { transform: 'translate(-100%, 0%)', opacity: '0' },
        },
        'star-movement-top': {
          '0%':   { transform: 'translate(0%, 0%)', opacity: '1' },
          '100%': { transform: 'translate(100%, 0%)', opacity: '0' },
        },
        glitch: {
          '0%':   { 'clip-path': 'inset(20% 0 50% 0)' },
          '5%':   { 'clip-path': 'inset(10% 0 60% 0)' },
          '10%':  { 'clip-path': 'inset(15% 0 55% 0)' },
          '15%':  { 'clip-path': 'inset(25% 0 35% 0)' },
          '20%':  { 'clip-path': 'inset(30% 0 40% 0)' },
          '25%':  { 'clip-path': 'inset(40% 0 20% 0)' },
          '30%':  { 'clip-path': 'inset(10% 0 60% 0)' },
          '35%':  { 'clip-path': 'inset(15% 0 55% 0)' },
          '40%':  { 'clip-path': 'inset(25% 0 35% 0)' },
          '45%':  { 'clip-path': 'inset(30% 0 40% 0)' },
          '50%':  { 'clip-path': 'inset(20% 0 50% 0)' },
          '55%':  { 'clip-path': 'inset(10% 0 60% 0)' },
          '60%':  { 'clip-path': 'inset(15% 0 55% 0)' },
          '65%':  { 'clip-path': 'inset(25% 0 35% 0)' },
          '70%':  { 'clip-path': 'inset(30% 0 40% 0)' },
          '75%':  { 'clip-path': 'inset(40% 0 20% 0)' },
          '80%':  { 'clip-path': 'inset(20% 0 50% 0)' },
          '85%':  { 'clip-path': 'inset(10% 0 60% 0)' },
          '90%':  { 'clip-path': 'inset(15% 0 55% 0)' },
          '95%':  { 'clip-path': 'inset(25% 0 35% 0)' },
          '100%': { 'clip-path': 'inset(30% 0 40% 0)' },
        },
        shine: {
          '0%':   { 'background-position': '100%' },
          '100%': { 'background-position': '-100%' },
        },
      },
      animation: {
        shine: 'shine 5s linear infinite',
        'glitch-after': 'glitch var(--after-duration) infinite linear alternate-reverse',
        'glitch-before': 'glitch var(--before-duration) infinite linear alternate-reverse',
        'star-movement-bottom': 'star-movement-bottom linear infinite alternate',
        'star-movement-top':    'star-movement-top    linear infinite alternate',
      },
    },
  },
  
  plugins: [],
}

