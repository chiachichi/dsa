"""
draw_ruler module

This module is used to draw a ruler.
"""


# 因為會重複進行繪製刻度的動作，所以寫一個函數負責繪製刻度
def draw_tick(tick_length: int, tick_label: str = ""):
    """基於長度及可選的標籤繪製刻度"""
    tick = "-" * tick_length
    if tick_label:
        tick += " " + tick_label
    print(tick)


# 遞迴函數
def draw_interval(center_length: int):
    """基於中間刻度長度畫一個區間"""
    if center_length > 0:
        draw_interval(center_length-1)
        draw_tick(center_length)
        draw_interval(center_length-1)


# 主程式接口
def draw_ruler(major_tick_length: int, max_inch: int):
    """基於最大刻度長度及最大英吋繪製尺"""
    draw_tick(major_tick_length, "0")
    for inch in range(1, max_inch+1):
        draw_interval(major_tick_length-1)
        draw_tick(major_tick_length, str(inch))