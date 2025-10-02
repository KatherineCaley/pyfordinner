#!/usr/bin/env python3

RESET = "\033[0m"
BOLD = "\033[1m"
# El Pato label yellow ≈ #ECB44D (RGB 236,180,77)
BG_YELLOW = "\033[48;2;236;180;77m"
BG_GREEN = "\033[42m"
BG_RED = "\033[41m"

WIDTH = 48

def _center_left_offset(inner_width: int) -> int:
    return max((WIDTH - inner_width) // 2, 0)

def _print_bg_block_line(left_pad: int, width: int, bg_color: str) -> None:
    print(f"{' ' * left_pad}{bg_color}{' ' * width}{RESET}")

def _print_label_border_line(left_pad: int, body_width: int, label_width: int, border: int = 1) -> None:
    # Only a green stripe across the top of the label area
    print(f"{' ' * left_pad}{BG_GREEN}{' ' * body_width}{RESET}")

def _print_label_text_line(left_pad: int, body_width: int, label_width: int, text: str, border: int = 1) -> None:
    # Yellow label wraps fully around (no visible side borders)
    pad_total = max(body_width - len(text), 0)
    lpad = pad_total // 2
    rpad = body_width - len(text) - lpad
    print(
        f"{' ' * left_pad}"
        f"{BG_YELLOW}{' ' * lpad}{BOLD}{text}{RESET}{BG_YELLOW}{' ' * rpad}{RESET}"
    )

def print_el_pato_bottle():
    # Cap (yellow)
    cap_w = 6
    for _ in range(2):
        _print_bg_block_line(_center_left_offset(cap_w), cap_w, BG_YELLOW)
    # Neck (red)
    neck_w = 6
    for _ in range(2):
        _print_bg_block_line(_center_left_offset(neck_w), neck_w, BG_RED)
    # Shoulders widen (red)
    for w in (8, 10, 12, 16, 18):
        _print_bg_block_line(_center_left_offset(w), w, BG_RED)
    body_w = 18  # skinnier bottle
    # Upper body (red)
    for _ in range(2):
        _print_bg_block_line(_center_left_offset(body_w), body_w, BG_RED)
    # Label block (yellow wrap with green top border)
    label_w = body_w
    left_pad = _center_left_offset(body_w)
    _print_label_border_line(left_pad, body_w, label_w)
    _print_label_text_line(left_pad, body_w, label_w, "EL PATO")
    _print_label_text_line(left_pad, body_w, label_w, "🦆")
    _print_label_text_line(left_pad, body_w, label_w, "HOT SAUCE")
    _print_label_border_line(left_pad, body_w, label_w)
    # Lower body (red)
    for _ in range(3):
        _print_bg_block_line(_center_left_offset(body_w), body_w, BG_RED)
    # Base taper (red)
    for w in (16, 12):
        _print_bg_block_line(_center_left_offset(w), w, BG_RED)

if __name__ == "__main__":
    print_el_pato_bottle()