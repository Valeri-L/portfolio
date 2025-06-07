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
  <div class="bg-primary-200 flex flex-col rounded-lg shadow-lg mt-[12rem] mx-[8rem]" >

    <!-- About Me Section -->
    <section id="about-me" class="h-screen">
      <AboutMe />
    </section>

    <!-- Skills Section -->
    <section id="skills" class="h-auto">
      <Skills />
    </section>

    <!-- What I Do Section -->
    <section id="what_i_do" class="h-screen">
      <WhatIDo />
    </section>

    <!-- Achievements Section -->
    <!-- <section id="achievements" class="h-screen">
      <Achievements />
    </section> -->

    <!-- Projects Section -->
    <section id="projects" class="h-screen pt-[40rem]">
      <Projects />
    </section>

    <!-- Contact Me Section -->
    <section id="contact-me" class="h-screen mb-10">
      <ContactMe />
    </section>
  </div>
</template>

<style scoped>
</style>