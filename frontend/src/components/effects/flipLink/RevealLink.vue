<template>
    <section class="reveal-links  ">
      <FlipLink
        v-for="(item,i) in links"
        :key="i"
        :href="item.href"
        :label="item.label"
        :copyable="item.copyable"
        :copyText="item.copyText"
      />
    </section>
  </template>
  
  <script setup>
  import FlipLink from './FlipLink.vue'
  
  const links = [
        { href: 'https://instagram.com/valeri_levinson',label: 'INSTAGRAM',copyable: false},
        { href: 'https://www.facebook.com/valery.levinson',label: 'FACEBOOK',copyable: false},
        { href: 'https://www.linkedin.com/in/valeri-levinson-643654350',  label: 'LINKEDIN',copyable: false  },
        { href: '#',copyText:'levinsonvaleri@gmail.com',label: 'EMAIL', copyable: true},
        { href: '#',label: 'PHONE',copyText:'+972-055-225-1273', copyable: true},
  ]
  </script>
  
  <style scoped>
  .reveal-links {
    display: grid;
    place-content: start;
    justify-content: start;


    
  }
  
  </style>
  