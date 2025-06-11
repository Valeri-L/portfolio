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
  <!-- About Me Section -->
  <section id="about-me" class="about-me-section h-screen bg-primary-200">
    <AboutMe />
  </section>

  <div  class="all-sections bg-primary-200 flex flex-col  shadow-lg relative overflow-hidden"
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

  
}

@media (min-width:1024px) {
  
  .about-me-section {
    margin: 0rem 8rem;
  }

  .all-sections {
    margin: 0rem 8rem;
}

}

.all-sections {

}


</style>