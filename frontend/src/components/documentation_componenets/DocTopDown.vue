<template>
  <h1 class="header_large"> <span class="capitalize font-bold">First Steps to Programming :</span> Building a Pixel Art Game</h1>
    <div class="flex flex-col gap-14">
       <!-- main header -->
       <div class="introduction_section">
         <h2 class="header_medium">Introduction</h2>
         <p class="text_regular">When I first started learning programming, I found myself jumping from one tutorial to another and completing courses without truly understanding the concepts. I realized that the best way to learn was to take on a challenging project—one that would push me to apply what I’d learned and uncover new skills along the way. That’s when I decided to build a pixel art game using Python.</p>
         <p class="text_regular">Game development turned out to be the perfect starting point for exploring essential programming concepts like Object-Oriented Programming (OOP). For instance, creating a class called Monster and then extending it to create specific types like Vampire or Orc taught me about inheritance and how to reuse and extend code efficiently.</p>
         <p class="text_regular">Building a game involves much more than just coding classes—it’s about planning, structuring code, and tackling unexpected challenges. This project turned into an exciting journey into programming fundamentals and game development, where I explored a wealth of free assets available online. I even used tools to resize and edit images, ensuring compatibility across assets from various sources.</p>
         <p class="text_regular">Throughout the process, I gained valuable technical skills: applying Object-Oriented Programming (OOP) principles, managing frames-per-second (FPS), working with sprites, animating images, and leveraging geometry to implement features like shooting arrows and fireballs. I also discovered that planning and managing assets is far more complex than it initially seems, making the entire experience both challenging and rewarding.</p>
       </div>

       <div class="overview_section">
         <h2 class="header_medium">Project Overview</h2>
         <p class="text_regular">The goal was to create a top-down game with simple pixel art, featuring a player navigating through levels, battling monsters, and casting spells. Along the way, I used Pygame, a Python game development library, to bring the game to life.</p>
         <p class="text_regular">To make the game visually appealing, I researched free pixel art assets and learned how to modify them to fit my needs. I also explored tools for creating tile-based maps and animations, which added depth and character to the game.</p>
       </div>



       <div class="features_section">
        <h2 class="header_medium">Key Features</h2>
        <p class="mb-4">Here are some highlights of the project:</p>
        <ul class="list-disc list-inside space-y-4">
          <!-- Mechanics Section -->
          <li>
            <span class="header_ul">Custom Gameplay Mechanics:</span>
            <ul class="nested_ul">
              <li>
                Implemented movement, attacks, and spell animations.  
              </li>
              <li>
                Designed and programmed projectiles like arrows and fireballs using basic geometry and physics.
              </li>
            </ul>
          </li>
          <!-- Pixel Art Section -->
          <li>
            <span class="header_ul">Pixel Art Integration:</span>
            <ul class="nested_ul">
              <li>
                Sourced and resized assets to create a cohesive style.
              </li>
              <li>
                Built maps with tile-based editors for a polished top-down perspective.
              </li>
            </ul>
          </li>
          <!-- Performance Section -->
          <li>
            <span class="header_ul">Optimized Performance:</span>
            <ul class="nested_ul">
              <li>
                Learned how to handle Frames Per Second (FPS) for smooth gameplay.
              </li>
              <li>
                Managed sprite animations and interactions for responsive mechanics.
              </li>
            </ul>
          </li>
          
        </ul>
        <p class="text_regular">These skills had to be learned in order to develop the application successfully and deliver a well-executed project, and I enjoyed the process of learning new things along the way.</p>
      </div>




       <div class="challenges_section">
        <h2 class="header_medium">Challenges and Lessons Learned</h2>
        <!-- <p class="text_regular">The project wasn’t without its challenges:</p> -->
        <ul class="header_ul_regular">
          <li><span class="font-semibold">Understanding Object-Oriented Programming (OOP):</span> Learning to design reusable and efficient code structures.</li>
          <li><span class="font-semibold">Handling FPS and Animations: </span>Ensuring smooth gameplay required studying Pygame’s documentation and experimenting with performance optimization.</li>
          <li><span class="font-semibold">Mathematics in Game Development:</span>Implementing mechanics like projectile trajectories demanded basic geometry and problem-solving.</li>
        </ul>
        <p class="text_regular">These challenges taught me the importance of persistence, research, and planning. Watching tutorials, reading documentation, and troubleshooting problems were all invaluable parts of the learning process.</p>
      </div>
     
      <div class="why_section">
        <h2 class="header_medium">Why This Project Mattered</h2>
        <p class="text_regular">This project wasn’t just about creating a game; it was about building a strong foundation in programming. From understanding how to structure code to exploring visual design and performance optimization, I gained skills that will benefit me in any software development field.</p>
        <p class="text_regular">It also showed me how much fun programming can be when applied to creative projects. Whether you’re new to coding or looking for a rewarding challenge, building something like this is a great way to learn and grow.</p>
      </div>

      <div class="plan_section">
        <h2 class="header_medium">Challenges</h2>
        <p class="text_regular">The main challenges I faced were understanding FPS handling, applying mathematics to gameplay mechanics, animating sprites, and mastering OOP concepts. Overcoming these hurdles required a lot of perseverance, reading Pygame documentation, and watching countless tutorials.</p>
      </div>

    </div>
   </template>
   
   <script setup>
   </script>
   
   <style scoped>
   /* Add any styles here */
     .header_large {
       @apply text-primary-300  font-roboto my-12
     }
     .header_medium {
       @apply text-primary-300  font-roboto font-bold my-4 capitalize
     }
     .text_regular {
       @apply text-primary-300 leading-7 font-roboto  my-4 ml-2
     }
     .nested_ul {
       @apply list-disc pl-10 space-y-2 mt-2
     }
     .header_ul {
       @apply font-bold text-lg underline underline-offset-8
     }
     .header_ul_regular {
       @apply list-disc list-outside space-y-2 ml-2
     }
   </style>
   