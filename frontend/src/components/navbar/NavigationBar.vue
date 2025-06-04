<script setup>
import { ref } from 'vue';
import { useLanguage } from '../../composables/useLanguage';
const activeButton = ref(null);
const { getText } = useLanguage()
const { lang, setLanguage } = useLanguage()

const toggleLang = () => {
  const newLang = lang.value === 'en' ? 'he' : 'en'
  setLanguage(newLang)
}


const showSideBar = () => {
  const sidebar = document.querySelector(".sidebar")
  sidebar.classList.add("active");

}



const hideSideBar = () => {
  const sidebar = document.querySelector(".sidebar")
  sidebar.classList.remove("active");
}

const closeBtn = () => {
  const sidebar = document.querySelector(".sidebar")
  sidebar.classList.remove("active");
}

const scrollTo = (section) => {
  const element = document.getElementById(section);
  if (element) {
    // Add a small timeout to ensure smooth scrolling completes before adjusting offset
    setTimeout(() => {
      // Adjust the scrolling offset
      const offset = -90; // Adjust this value as needed (e.g., for fixed navbar height)
      const y = element.getBoundingClientRect().top + window.pageYOffset + offset;
      window.scrollTo({ top: y, behavior: 'smooth' });
    }, 200);

    // Set the active button
    activeButton.value = section;
  }
};

const button_sx = "";
</script>

<template>

  <nav class="font-pixelify bg-primary-100 bg-opacity-80 border-b border-text-red border-opacity-30">
    <ul >
    
      <div class="flex mr-auto">
      <li class="">
        <div class="text-xl h-[100%] w-[12rem]">
          <button :class="button_sx" @click="scrollTo('about-me')">{{ getText('aboutMe.name') }}</button><!-- logo on the top left side -->
        </div>
      </li>


      <li class="flex items-center">
        <label for="langToggle" class="inline-flex items-center space-x-3 cursor-pointer text-primary-300">
          <span class="text-xs font-semibold">EN</span>
          <span class="relative">
            <input
              id="langToggle"
              type="checkbox"
              class="hidden peer"
              :checked="lang === 'he'"
              @change="toggleLang"
            />
            <div class="w-10 h-6 rounded-full shadow-inner bg-gray-400 peer-checked:bg-violet-600 transition-colors"></div>
            <div class="absolute inset-y-0 left-0 w-4 h-4 m-1 rounded-full bg-white shadow peer-checked:translate-x-full transform transition-transform"></div>
          </span>
          <span class="text-xs font-semibold">HE</span>
        </label>
      </li>
    </div>

      <li class="hideOnMobile">
        <button
          :class="` ${activeButton === 'about' ? 'no-underline' : ''}`"
          @click="scrollTo('about-me')"
        >{{ getText('nav.about') }}</button>
      </li>
      <li class="hideOnMobile">
        <button
          :class="` ${activeButton === 'what_i_do' ? 'no-underline' : ''}`"
          @click="scrollTo('what_i_do')"
        >{{ getText('nav.whatIDo') }}</button>
      </li>
      <li class="hideOnMobile">
        <button
          :class="` ${activeButton === 'achievements' ? 'no-underline' : ''}`"
          @click="scrollTo('achievements')"
        >{{ getText('nav.achievements') }}</button>
      </li>
      <li class="hideOnMobile">
        <button
          :class="` ${activeButton === 'projects' ? 'no-underline' : ''}`"
          @click="scrollTo('projects')"
        >{{ getText('nav.projects') }}</button>
      </li>
      <li class="hideOnMobile">
        <button
          :class="` ${activeButton === 'contact' ? 'no-underline' : ''}`"
          @click="scrollTo('contact-me')"
        >{{ getText('nav.contact') }}</button>
      </li>

      <li class="sidebar-button" :onclick="showSideBar">
        <button >
          <img src="/menuIcon.svg" alt="sidebar icon"></img>
        </button>
      </li>
    </ul>



    <ul class="sidebar">
      <!-- flex items-center justify-between px-6 py-4 -->
      <!-- flex items-center gap-8 -->
      <!-- logo -->
      <li :onclick="hideSideBar">
        <button >
          <img src="/arrowBack.svg" alt="close icon"></img>
        </button>
      </li>

      <li>
        <button
          :class="`${button_sx} ${activeButton === 'about' ? 'no-underline' : ''}`"
          @click="scrollTo('about-me');closeBtn()"
        >About Me</button>
      </li>
      <li>
        <button
          :class="`${button_sx} ${activeButton === 'what_i_do' ? 'no-underline' : ''}`"
          @click="scrollTo('what_i_do');closeBtn()"
        >What I Do</button>
      </li>
      <li>
        <button
          :class="`${button_sx} ${activeButton === 'achievements' ? 'no-underline' : ''}`"
          @click="scrollTo('achievements');closeBtn()"
        >Achievements</button>
      </li>
      <li>
        <button
          :class="`${button_sx} ${activeButton === 'projects' ? 'no-underline' : ''}`"
          @click="scrollTo('projects');closeBtn()"
        >Projects</button>
      </li>
      <li>
        <button
          :class="`${button_sx} ${activeButton === 'contact' ? 'no-underline' : ''}`"
          @click="scrollTo('contact-me');closeBtn()"
        >Contact Me</button>
      </li>
    </ul>
  </nav>

</template>

<style scoped>
  nav {
    background-color: "#f7f7f7";
    box-shadow: 3px 3px 5px rgba(0,0,0,0.1);
    width:100%;
    position: fixed;
    overflow-x: hidden;

  }
  
  nav ul {
    display: flex;
    align-items:center;
    padding: 0.5rem;
  }
  
  nav li {
    height: 50px;
    text-wrap: nowrap;
  }

  nav button {
  height: 100%;
  padding: 0 0.8rem;
  background-color:transparent;
  border: none;
  transition-duration: 0.4s;
  }

  nav button:hover {
    text-decoration: underline;
    text-decoration-color: #ce7fe4;
    text-decoration-thickness: 2px;
    text-underline-offset: 6px;
    opacity:8;
  }

  nav button:focus {
    outline: none;
    text-decoration: underline;
    text-decoration-color: #ce7fe4;
    text-decoration-thickness: 2px;
    text-underline-offset: 6px;
    opacity:8;
  }

  nav li:nth-child(1) {
    margin-right: auto ;
    
    
  }

  .sidebar {
    position: fixed;
    top: 0;
    right: 0;
    height: 100vh;
    width: 250px;
    z-index: 999;
    background-color: rgba(26, 26, 26, 0.592);
    box-shadow: -10px 0 -10px rgba(0,0,0,0.1);
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    backdrop-filter: blur(10px);
    overflow-x: hidden;

    /* Animation */
    transform: translateX(100%); /* Start off-screen */
    transition: transform 0.3s ease-in-out;


  }
  .sidebar.active {
    transform: translateX(0);
  }
  .sidebar li {
    width: 100%;
  }


  .sidebar button {
    width: 100%;
  }

  .sidebar-button{
    display: none;
    height: 100%;
    
  }



  @media(max-width :930px) {
    .hideOnMobile{
      display: none;
    }
    .sidebar-button {
      display: block;
    }
  }

  @media(max-width :400px) {
    .sidebar {
      width: 100%;
    }
  }


</style>
