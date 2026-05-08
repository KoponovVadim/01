<template>

  <transition name="popup-fade">

    <div
      v-if="isOpen"
      class="lead-popup"
      @click="closePopup"
    >

      <!-- WINDOW -->

      <div
        class="lead-popup__window"
        @click.stop
      >

        <!-- CLOSE -->

        <button
          class="lead-popup__close"
          type="button"
          @click="closePopup"
        >
          ×
        </button>

        <!-- TOP -->

        <div class="lead-popup__top">

          <span class="lead-popup__label">
            заявка
          </span>

          <h2 class="lead-popup__title">
            ОБСУДИМ<br />
            ВАШ ПРОЕКТ
          </h2>

          <p class="lead-popup__description">
            Ответим, зададим пару вопросов
            и предложим решение под ваш проект.
          </p>

        </div>

        <!-- FORM -->

        <form
          class="lead-popup__form"
          @submit.prevent="submitForm"
        >

          <!-- NAME -->

          <div class="lead-popup__field">

            <label>
              ваше имя
            </label>

            <input
              v-model="form.name"
              type="text"
              placeholder="как к вам обращаться?"
              required
            />

          </div>

          <!-- CONTACT -->

          <div class="lead-popup__field">

            <label>
              контакт
            </label>

            <input
              v-model="form.contact"
              type="text"
              placeholder="telegram или телефон"
              required
            />

          </div>

          <!-- MESSAGE -->

          <div class="lead-popup__field">

            <label>
              задача
            </label>

            <textarea
              v-model="form.message"
              placeholder="кратко опишите проект"
              rows="4"
            ></textarea>

          </div>

          <!-- SUBMIT -->

          <button
            type="submit"
            class="lead-popup__submit"
            :disabled="loading"
          >

            {{ loading ? 'отправляем...' : 'отправить заявку' }}

          </button>

          <!-- SUCCESS -->

          <div
            v-if="success"
            class="lead-popup__success"
          >
            Заявка отправлена. Скоро свяжемся.
          </div>

        </form>

      </div>

    </div>

  </transition>

</template>

<script setup>
import {
  ref,
  reactive,
  onMounted,
  onUnmounted,
} from 'vue';

/* ======================================
   STATE
====================================== */

const isOpen = ref(false);

const loading = ref(false);

const success = ref(false);

/* ======================================
   FORM
====================================== */

const form = reactive({
  name: '',
  contact: '',
  message: '',
});

/* ======================================
   OPEN
====================================== */

const openPopup = () => {

  isOpen.value = true;

  document.body.style.overflow = 'hidden';

};

/* ======================================
   CLOSE
====================================== */

const closePopup = () => {

  isOpen.value = false;

  setTimeout(() => {
    document.body.style.overflow = '';
  }, 250);

};

/* ======================================
   ESC CLOSE
====================================== */

const handleEscape = (e) => {

  if (e.key === 'Escape') {
    closePopup();
  }

};

/* ======================================
   SUBMIT
====================================== */

const submitForm = async () => {

  loading.value = true;

  try {

    const response = await fetch('/api/lead', {

      method: 'POST',

      headers: {
        'Content-Type': 'application/json',
      },

      body: JSON.stringify({
        name: form.name,
        contact: form.contact,
        message: form.message,
      }),

    });

    if (!response.ok) {
      throw new Error('Ошибка отправки');
    }

    success.value = true;

    form.name = '';
    form.contact = '';
    form.message = '';

    setTimeout(() => {

      success.value = false;

      closePopup();

    }, 1800);

  } catch (err) {

    console.error(err);

    alert('Ошибка отправки формы');

  } finally {

    loading.value = false;

  }

};

/* ======================================
   LIFECYCLE
====================================== */

onMounted(() => {

  window.addEventListener(
    'open-popup',
    openPopup
  );

  document.addEventListener(
    'keydown',
    handleEscape
  );

});

onUnmounted(() => {

  window.removeEventListener(
    'open-popup',
    openPopup
  );

  document.removeEventListener(
    'keydown',
    handleEscape
  );

});
</script>

<style lang="scss">
.lead-popup {
  position: fixed;
  inset: 0;

  z-index: 999;

  display: flex;
  align-items: center;
  justify-content: center;

  padding: 20px;

  background:
    rgba(5,7,11,.74);

  backdrop-filter: blur(14px);

  /* ======================================
     WINDOW
  ====================================== */

  &__window {
    position: relative;

    width: 100%;
    max-width: 520px;

    padding:
      34px
      34px
      30px;

    overflow: hidden;

    border:
      1px solid rgba(255,255,255,.06);

    border-radius: 28px;

    background:
      linear-gradient(
        180deg,
        rgba(9,12,18,.96) 0%,
        rgba(5,7,11,.98) 100%
      );

    box-shadow:
      0 30px 80px rgba(0,0,0,.45);

    @media (max-width: 768px) {
      padding:
        26px
        20px
        22px;

      border-radius: 22px;
    }
  }

  /* ======================================
     GLOW
  ====================================== */

  &__window::before {
    content: '';

    position: absolute;

    top: -120px;
    right: -120px;

    width: 260px;
    height: 260px;

    border-radius: 50%;

    background:
      radial-gradient(
        rgba(217,255,0,.12),
        transparent 70%
      );

    pointer-events: none;
  }

  /* ======================================
     CLOSE
  ====================================== */

  &__close {
    position: absolute;

    top: 16px;
    right: 16px;

    width: 42px;
    height: 42px;

    display: flex;
    align-items: center;
    justify-content: center;

    border:
      1px solid rgba(255,255,255,.06);

    border-radius: 12px;

    background:
      rgba(255,255,255,.03);

    color:
      rgba(255,255,255,.72);

    font-size: 22px;

    cursor: pointer;

    transition:
      .25s ease;

    &:hover {
      color: #d9ff00;

      border-color:
        rgba(217,255,0,.18);

      background:
        rgba(217,255,0,.06);
    }
  }

  /* ======================================
     TOP
  ====================================== */

  &__top {
    margin-bottom: 26px;
  }

  &__label {
    display: inline-flex;
    align-items: center;

    gap: 10px;

    margin-bottom: 18px;

    color: #d9ff00;

    font-size: 10px;
    font-weight: 700;

    letter-spacing: .16em;

    text-transform: uppercase;

    &::before {
      content: '';

      width: 6px;
      height: 6px;

      border-radius: 50%;

      background: #d9ff00;

      box-shadow:
        0 0 10px rgba(217,255,0,.8);
    }
  }

  &__title {
    margin-bottom: 16px;

    color: #fff;

    font-family:
      'Tektur',
      sans-serif;

    font-size:
      clamp(34px, 4vw, 56px);

    font-weight: 800;

    line-height: .92;

    letter-spacing: -.05em;

    text-transform: uppercase;
  }

  &__description {
    max-width: 360px;

    color:
      rgba(255,255,255,.56);

    font-size: 14px;

    line-height: 1.7;
  }

  /* ======================================
     FORM
  ====================================== */

  &__form {
    display: flex;
    flex-direction: column;

    gap: 18px;
  }

  &__field {
    display: flex;
    flex-direction: column;

    gap: 10px;

    label {
      color:
        rgba(255,255,255,.42);

      font-size: 11px;
      font-weight: 600;

      letter-spacing: .08em;

      text-transform: uppercase;
    }

    input,
    textarea {
      width: 100%;

      border:
        1px solid rgba(255,255,255,.06);

      border-radius: 16px;

      background:
        rgba(255,255,255,.03);

      color: #fff;

      padding:
        16px
        18px;

      font-size: 14px;

      outline: none;

      resize: none;

      transition:
        border-color .25s ease,
        background .25s ease;

      &::placeholder {
        color:
          rgba(255,255,255,.28);
      }

      &:focus {
        border-color:
          rgba(217,255,0,.24);

        background:
          rgba(255,255,255,.04);
      }
    }

    textarea {
      min-height: 120px;
    }
  }

  /* ======================================
     SUBMIT
  ====================================== */

  &__submit {
    width: 100%;
    height: 56px;

    border: none;

    border-radius: 16px;

    background: #d9ff00;

    color: #05070b;

    font-size: 14px;
    font-weight: 700;

    cursor: pointer;

    box-shadow:
      0 0 30px rgba(217,255,0,.14);

    transition:
      transform .25s ease,
      box-shadow .25s ease,
      opacity .25s ease;

    &:hover {
      transform:
        translateY(-2px);

      box-shadow:
        0 0 40px rgba(217,255,0,.22);
    }

    &:disabled {
      opacity: .6;

      cursor: default;
    }
  }

  /* ======================================
     SUCCESS
  ====================================== */

  &__success {
    padding:
      14px
      16px;

    border:
      1px solid rgba(217,255,0,.14);

    border-radius: 14px;

    background:
      rgba(217,255,0,.06);

    color: #d9ff00;

    font-size: 13px;

    line-height: 1.6;
  }
}

/* ======================================
   TRANSITIONS
====================================== */

.popup-fade-enter-active,
.popup-fade-leave-active {
  transition:
    opacity .25s ease;
}

.popup-fade-enter-from,
.popup-fade-leave-to {
  opacity: 0;
}
</style>