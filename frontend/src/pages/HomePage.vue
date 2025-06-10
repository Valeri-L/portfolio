<script setup>
import AboutMe from '../components/homepage/AboutMe.vue';
import Achievements from '../components/homepage/Achievements.vue';
import ContactMe from '../components/homepage/ContactMe.vue';
import NavigationBar from '../components/navbar/NavigationBar.vue';
import Projects from '../components/homepage/Projects.vue';
import Skills from '../components/homepage/Skills.vue';
import WhatIDo from '../components/homepage/WhatIDo.vue';
</script>


<template>
      <!-- Top navigation bar -->
  <header class="fixed top-0 left-0 w-full z-10">
    <NavigationBar />
  </header>
  <!-- px-0 md:px-10 lg:px-20 md:p-0 -->
  <!-- Content of the page -->
  <!-- About Me Section -->
  <section id="about-me" class="about-me-section h-screen mt-[12rem] mx-[8rem] bg-primary-200">
    <AboutMe />
  </section>

  <div  class="bg-primary-200 flex flex-col  shadow-lg mx-[8rem] relative overflow-hidden"
    >


    <!-- What I Do Section -->
    <section id="what_i_do" class="">
      <WhatIDo />
    </section>

    <!-- Projects Section -->
    <section id="projects" class="pt-[20rem]">
      <Projects />
    </section>

    <!-- Skills Section -->
    <section id="skills" class="mt-40">
      <Skills />
    </section>

    <!-- Contact Me Section -->
    <section id="contact-me" class="h-screen">
      <ContactMe />
    </section>
  </div>
</template>

<style scoped>
.about-me-section {
  /* Allow any child to overflow beyond the 8rem gutters */
  overflow: visible !important;
}
</style>