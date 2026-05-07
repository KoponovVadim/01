<template>
  <section class="tabs">

    <div class="container">

      <!-- TOP -->

      <div class="tabs__top">

        <div class="tabs__left">

          <span class="tabs__label">
            концепты
          </span>

          <h2 class="tabs__title">
            ГОТОВЫЕ
            <br />
            ВКЛАДКИ
          </h2>

        </div>

        <div class="tabs__right">

          <p class="tabs__description">
            Готовые концепты сайтов и интерфейсов,
            которые можно адаптировать под ваш проект.
          </p>

          <div class="tabs__controls">

            <div class="tabs__counter">

              <strong>
                06
              </strong>

              <span>
                концептов
              </span>

            </div>

            <div class="tabs__buttons">

              <button
                class="tabs__button"
                type="button"
                @click="scrollPrev"
              >
                ←
              </button>

              <button
                class="tabs__button"
                type="button"
                @click="scrollNext"
              >
                →
              </button>

            </div>

          </div>

        </div>

      </div>

      <!-- SLIDER -->

      <div
        ref="slider"
        class="tabs__slider"
      >

        <article
          v-for="(tab, index) in tabs"
          :key="index"
          class="tab-card"
          @click="openModal(tab.image)"
        >

          <div class="tab-card__image">

            <img
              :src="tab.image"
              :alt="tab.title"
            />

          </div>

          <div class="tab-card__overlay"></div>

          <div class="tab-card__top">

            <span class="tab-card__number">
              0{{ index + 1 }}
            </span>

          </div>

          <div class="tab-card__content">

            <div>

              <h3 class="tab-card__title">
                {{ tab.title }}
              </h3>

              <span class="tab-card__meta">
                {{ tab.meta }}
              </span>

            </div>

            <span class="tab-card__arrow">
              ↗
            </span>

          </div>

        </article>

      </div>

    </div>

    <!-- MODAL -->

    <div
      v-if="activeImage"
      class="tabs-modal"
      @click="closeModal"
    >

      <div
        class="tabs-modal__content"
        @click.stop
      >

        <button
          class="tabs-modal__close"
          @click="closeModal"
          type="button"
        >
          ×
        </button>

        <img
          :src="activeImage"
          alt=""
        />

      </div>

    </div>

  </section>
</template>

<script setup>
import { ref } from 'vue';

const slider = ref(null);

const activeImage = ref(null);

const tabs = [
  {
    title: 'КОЖАЕД.РФ',
    meta: 'косметология',
    image: '/images/tab_1.webp',
  },

  {
    title: 'НЕСПЯЩИЕ.РФ',
    meta: 'кальян-бар',
    image: '/images/tab_2.webp',
  },

  {
    title: 'ЗАВОД.РФ',
    meta: 'промышленный сайт',
    image: '/images/tab_3.webp',
  },

  {
    title: 'REBOOT.РФ',
    meta: 'ремонт приставок',
    image: '/images/tab_4.webp',
  },

  {
    title: 'CTRL+HELP.РФ',
    meta: 'it-помощь',
    image: '/images/tab_5.webp',
  },

  {
    title: 'PRINT+PLAY.РФ',
    meta: 'типография',
    image: '/images/tab_6.webp',
  },
];

const getCardWidth = () => {

  if (!slider.value) return 0;

  const card = slider.value.querySelector('.tab-card');

  if (!card) return 0;

  const gap = parseFloat(
    getComputedStyle(slider.value).gap
  );

  return card.offsetWidth + gap;
};

const scrollNext = () => {

  if (!slider.value) return;

  slider.value.scrollBy({
    left: getCardWidth(),
  });
};

const scrollPrev = () => {

  if (!slider.value) return;

  slider.value.scrollBy({
    left: -getCardWidth(),
  });
};

const openModal = (image) => {

  activeImage.value = image;

  document.body.style.overflow = 'hidden';
};

const closeModal = () => {

  activeImage.value = null;

  document.body.style.overflow = '';
};
</script>
 