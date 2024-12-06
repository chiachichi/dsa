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
    if not isinstance(major_tick_length, int):
        raise TypeError("`major_tick_length` must be an integer.")
    if not isinstance(max_inch, int):
        raise TypeError("`max_inch` must be an integer.")
    if major_tick_length <= 0:
        raise ValueError("`major_tick_length` must be positive.")
    if max_inch < 0:
        raise ValueError("`max_inch` must be non-negative.")
    draw_tick(major_tick_length, "0")
    for inch in range(1, max_inch+1):
        draw_interval(major_tick_length-1)
        draw_tick(major_tick_length, str(inch))


if __name__ == "__main__":
    draw_ruler(major_tick_length=4, max_inch=2)
    print("*" * 50)
    draw_ruler(major_tick_length=5, max_inch=1)
    print("*" * 50)
    draw_ruler(major_tick_length=3, max_inch=3)
    print("*" * 50)
    draw_ruler(major_tick_length=3, max_inch=0)