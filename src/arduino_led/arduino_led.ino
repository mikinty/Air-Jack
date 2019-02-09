#include <FastLED.h>
#define BUTTON      8
#define LED_PIN     6
#define NUM_LEDS    160

#define HEIGHT 8
#define WIDTH 16

CRGB leds[NUM_LEDS];
int mode = 0;
int TOTAL_MODES = 5;
int curr_snake = 0;

static const uint8_t music_note[8][16] = {
  {0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0},
  {1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1},
  {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
  {0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1},
  {0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0},
  {0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
};


void setup() {
  FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, NUM_LEDS);
  pinMode(BUTTON, INPUT);
  Serial.begin(9600);
}

void draw_note() {
  for (int i = 0; i < HEIGHT; i++) {
    for (int j = 0; j < WIDTH; j++) {
      if (music_note[i][j] == 1) {
        leds[i*WIDTH + j] = CRGB(255, 255, 255);
      } else {
        leds[i*WIDTH + j] = CRGB(0, 0, 0);
      }
    }
  }
  FastLED.show();
}

void clear_screen() {
  for (int i = 0; i < NUM_LEDS; i++) {
    leds[i] = CRGB(0, 0, 0);
  }
  FastLED.show();
}

void draw_snake() {
  leds[curr_snake] = CRGB(255, 255, 255);
  curr_snake++;
  FastLED.show();
}

void draw_stripes() {
  for (int i = 0; i < NUM_LEDS; i++) {
    if (i % 2 == 0)
      leds[i] = CRGB(0, 0, 0);
    else {
      leds[i] = CRGB(255, 255, 255);
    }
  }
  FastLED.show();
}

void draw_colors() {
  for (int i = 0; i < NUM_LEDS; i++) {
    leds[i] = CRGB(random(256), random(256), random(256));
  }
  FastLED.show();
}

void strobe() {
  for (int i = 0; i < NUM_LEDS; i++) {
    if (random(2) > 0) {
      leds[i] = CRGB(255, 255, 255);
    }
    else {
      leds[i] = CRGB(0, 0, 0);
    }
  }
  FastLED.show();
}

void loop() {
  // button press
  if (digitalRead(BUTTON) == LOW) {
    mode = (mode + 1) % TOTAL_MODES;
    Serial.println("BUTTON PRESSED. Switch  to mode");
    Serial.println(mode);
    
    if (mode == 1) {
      curr_snake = 0;
    }

    clear_screen();
  }
  
  switch (mode) {
    case 1: 
      draw_snake();
      break;
    case 2:
      draw_stripes();
      break;
    case 3:
      draw_colors();
      break;
    case 4:
      strobe();
      break;
    
    default: draw_note();
  }
  
  delay(50);
}
