#include "raylib.h"
#include "easings.h" // include test

int main()
{
  InitWindow(200, 200, "test");
  SetTargetFPS(60);

  if (WindowShouldClose())
    return -1;

  int easingTest = EaseQuadOut(255.f, /*start*/ 0.f, /*delta*/ 255.f, /*duration*/ 255.f);
  if (easingTest != 255)
    return -1;

  BeginDrawing();
  ClearBackground(BLACK);
  DrawFPS(10, 10);
  EndDrawing();
  CloseWindow();

  return 0;
}