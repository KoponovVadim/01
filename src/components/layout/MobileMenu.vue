<template>

  <!-- BURGER -->

  <button
    class="mobile-menu__burger"
    :class="{ active: isOpen }"
    @click="toggleMenu"
  >

    <span></span>
    <span></span>

  </button>

  <!-- OVERLAY -->

  <transition name="overlay">

    <div
      v-if="isOpen"
      class="mobile-menu__overlay"
      @click="closeMenu"
    ></div>

  </transition>

  <!-- MENU -->

  <transition name="menu">

    <div
      v-if="isOpen"
      class="mobile-menu"
    >

      <div class="mobile-menu__container">

        <!-- TOP -->

        <div class="mobile-menu__top">

          <div class="mobile-menu__logo">
            01вкладка<span>.рф</span>
          </div>

          <button
            class="mobile-menu__close"
            @click="closeMenu"
          >

            <svg
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
            >
              <path
                d="M18 6L6 18M6 6L18 18"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
              />
            </svg>

          </button>

        </div>

        <!-- GRID -->

        <div class="mobile-menu__grid">

          <!-- NAV -->

          <nav class="mobile-menu__nav">

            <a href="#" @click="closeMenu">

              <span class="num">
                01
              </span>

              <span class="text">
                проекты
              </span>

            </a>

            <a href="#" @click="closeMenu">

              <span class="num">
                02
              </span>

              <span class="text">
                услуги
              </span>

            </a>

            <a href="#" @click="closeMenu">

              <span class="num">
                03
              </span>

              <span class="text">
                о студии
              </span>

            </a>

            <a href="#" @click="closeMenu">

              <span class="num">
                04
              </span>

              <span class="text">
                процесс
              </span>

            </a>

            <a href="#" @click="closeMenu">

              <span class="num">
                05
              </span>

              <span class="text">
                цены
              </span>

            </a>

            <a href="#" @click="closeMenu">

              <span class="num">
                06
              </span>

              <span class="text">
                контакты
              </span>

            </a>

          </nav>

          <!-- SIDE -->

          <aside class="mobile-menu__side">

            <div class="mobile-contact">

              <div class="mobile-contact__item">

                <span class="label">
                  email
                </span>

                <a href="mailto:hello@01.me">
                  hello@01.me
                </a>

              </div>

              <div class="mobile-contact__item">

                <span class="label">
                  telegram
                </span>

                <a href="#">
                  @studio01
                </a>

              </div>

            </div>

          </aside>

        </div>

      </div>

    </div>

  </transition>

</template>

<script setup>
import { ref, watch } from 'vue';

const isOpen = ref(false);

const toggleMenu = () => {
  isOpen.value = !isOpen.value;
};

const closeMenu = () => {
  isOpen.value = false;
};

watch(isOpen, (value) => {

  if (value) {
    document.body.style.overflow = 'hidden';
  } else {
    document.body.style.overflow = '';
  }

});
</script>