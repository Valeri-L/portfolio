<script setup>
import AboutMe from './components/AboutMe.vue';
import Achievements from './components/achievements.vue';
import ContactMe from './components/ContactMe.vue';
import NavigationBar from './components/NavigationBar.vue';
import Projects from './components/Projects.vue';
import Skills from './components/Skills.vue';
import WhatIDo from './components/WhatIDo.vue';
</script>

<template>
  <!-- Top navigation bar -->
  <header class="fixed top-0 left-0 w-full z-10">
    <NavigationBar />
  </header>

  <!-- Content of the page -->
  <div class="bg-primary-200 mx-4 md:mx-10 lg:mx-20 md:p-0 rounded-lg shadow-lg mt-[180px]">
    <!-- Add padding-top to avoid overlap with fixed navbar -->

    <!-- About Me Section -->
    <section id="about-me" class="pt-0">
      <AboutMe />
    </section>

    <!-- Skills Section -->
    <section id="skills" class="pt-20">
      <Skills />
    </section>

    <!-- What I Do Section -->
    <section id="what_i_do" class="pt-20">
      <WhatIDo />
    </section>

    <!-- Achievements Section -->
    <section id="achievements" class="pt-20">
      <Achievements />
    </section>

    <!-- Projects Section -->
    <section id="projects" class="pt-20">
      <Projects />
    </section>

    <!-- Contact Me Section -->
    <section id="contact-me" class="pt-20 mb-10">
      <ContactMe />
    </section>
  </div>
</template>

<style scoped>
/* Optional: You can adjust global or section-specific styles here */
</style>
