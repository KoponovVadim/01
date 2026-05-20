<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';

const isOpen = ref(false);

const toggleMenu = () => {
  isOpen.value = !isOpen.value;
};

const closeMenu = () => {
  isOpen.value = false;
};

const handleClickOutside = (event) => {
  const dock = document.querySelector('.floating-contact');

  if (dock && !dock.contains(event.target)) {
    closeMenu();
  }
};

const openPopup = () => {
  closeMenu();

  const popupButton = document.querySelector('[data-popup]');

  if (popupButton) {
    popupButton.click();
  }
};

onMounted(() => {
  document.addEventListener('click', handleClickOutside);
});

onBeforeUnmount(() => {
  document.removeEventListener('click', handleClickOutside);
});
</script>

<template>

  <div
    class="floating-contact"
    :class="{ 'floating-contact--active': isOpen }"
  >

    <!-- MENU -->

    <Transition name="floating-menu">

      <div
        v-if="isOpen"
        class="floating-contact__menu"
      >

        <!-- TELEGRAM -->

        <a
          href="https://t.me/vkladka01"
          target="_blank"
          rel="noopener noreferrer"
          class="floating-contact__item"
        >

          <span class="floating-contact__text">
            telegram
          </span>

        </a>

        <!-- VK -->

        <a
          href="https://vk.com/01vkladka"
          target="_blank"
          rel="noopener noreferrer"
          class="floating-contact__item"
        >


          <span class="floating-contact__text">
            Вконтакте
          </span>

        </a>

        <!-- FORM -->

        <button
          type="button"
          class="floating-contact__item"
          @click="openPopup"
        >
 

          <span class="floating-contact__text">
            Форма
          </span>

        </button>

      </div>

    </Transition>

    <!-- TOGGLE -->

    <button
      type="button"
      class="floating-contact__toggle"
      aria-label="Открыть контакты"
      @click.stop="toggleMenu"
    >

      <svg
        v-if="!isOpen"
        viewBox="0 0 24 24"
        fill="none"
      >
        <path
          d="M21 15C21 16.0609 20.5786 17.0783 19.8284 17.8284C19.0783 18.5786 18.0609 19 17 19H7L3 21V7C3 5.93913 3.42143 4.92172 4.17157 4.17157C4.92172 3.42143 5.93913 3 7 3H17C18.0609 3 19.0783 3.42143 19.8284 4.17157C20.5786 4.92172 21 5.93913 21 7V15Z"
          stroke="currentColor"
          stroke-width="1.8"
          stroke-linejoin="round"
        />
      </svg>

      <svg
        v-else
        viewBox="0 0 24 24"
        fill="none"
      >
        <path
          d="M18 6L6 18"
          stroke="currentColor"
          stroke-width="1.8"
          stroke-linecap="round"
        />

        <path
          d="M6 6L18 18"
          stroke="currentColor"
          stroke-width="1.8"
          stroke-linecap="round"
        />
      </svg>

    </button>

  </div>

</template>

<style scoped lang="scss">

.floating-contact {
  position: fixed;

  right: 32px;
  bottom: 32px;

  z-index: 999;

  display: flex;
  flex-direction: column;
  align-items: flex-end;

  gap: 16px;

  &--active {

    .floating-contact__toggle {
      background:
        #d9ff00;

      color:
        #05070b;

      box-shadow:
        0 20px 60px rgba(217,255,0,.24);
    }
  }

  &__menu {
    display: flex;
    flex-direction: column;

    gap: 12px;
  }

  &__item {
    display: flex;
    align-items: center;

    gap: 14px;

    min-width: 210px;

    padding:
      16px
      18px;

    border:
      1px solid rgba(255,255,255,.08);

    border-radius: 22px;

    background:
      rgba(7,10,14,.82);

    backdrop-filter: blur(18px);

    color:
      #f3f5f7;

    text-decoration: none;

    cursor: pointer;

    transition:
      transform .3s ease,
      border-color .3s ease,
      background .3s ease;

    &:hover {
      transform:
        translateY(-4px);

      border-color:
        rgba(217,255,0,.2);

      background:
        rgba(12,16,22,.92);

      .floating-contact__icon {
        color:
          #d9ff00;
      }
    }
  }

  &__icon {
    display: flex;
    align-items: center;
    justify-content: center;

    flex-shrink: 0;

    width: 42px;
    height: 42px;

    border-radius: 14px;

    background:
      rgba(255,255,255,.04);

    color:
      rgba(255,255,255,.78);

    transition:
      color .3s ease;

    svg {
      width: 20px;
      height: 20px;
    }
  }

  &__text {
    font-size: 16px;
    font-weight: 600;

    letter-spacing: -.02em;
  }

  &__toggle {
    display: flex;
    align-items: center;
    justify-content: center;

    width: 72px;
    height: 72px;

    border:
      1px solid rgba(255,255,255,.08);

    border-radius: 50%;

    background:
      rgba(7,10,14,.88);

    backdrop-filter: blur(18px);

    color:
      #f3f5f7;

    cursor: pointer;

    transition:
      transform .3s ease,
      background .3s ease,
      color .3s ease,
      box-shadow .3s ease;

    box-shadow:
      0 20px 60px rgba(0,0,0,.28);

    &:hover {
      transform:
        translateY(-4px);

      border-color:
        rgba(217,255,0,.16);
    }

    svg {
      width: 28px;
      height: 28px;
    }
  }
}

/* ANIMATION */

.floating-menu-enter-active,
.floating-menu-leave-active {
  transition:
    opacity .3s ease,
    transform .3s ease;
}

.floating-menu-enter-from,
.floating-menu-leave-to {
  opacity: 0;

  transform:
    translateY(12px)
    scale(.96);
}

/* MOBILE */

@media (max-width: 768px) {

  .floating-contact {
    right: 16px;
    bottom: 16px;

    &__item {
      min-width: 180px;

      padding:
        14px
        16px;
    }

    &__toggle {
      width: 62px;
      height: 62px;

      svg {
        width: 24px;
        height: 24px;
      }
    }
  }
}

</style>