<script setup>
import AboutMe from './portfolio_components/AboutMe.vue';
import Achievements from './portfolio_components/Achievements.vue';
import ContactMe from './portfolio_components/ContactMe.vue';
import NavigationBar from './portfolio_components/NavigationBar.vue';
import Projects from './portfolio_components/Projects.vue';
import Skills from './portfolio_components/Skills.vue';
import WhatIDo from './portfolio_components/WhatIDo.vue';
</script>


<template>
      <!-- Top navigation bar -->
  <header class="fixed top-0 left-0 w-full z-10">
    <NavigationBar />
  </header>
  <!-- Content of the page -->
  <div >
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
</style>