extern crate bmp;

fn main() {
    let mut img = bmp::open("parrots.bmp").unwrap_or_else(|e| {
        panic!("Failed to open: {}", e);
    });
    for (x, y) in img.coordinates() {
        let px = img.get_pixel(x, y);

        let gray_color: u8 =
            (0.299 * px.r as f32 + 0.587 * px.g as f32 + 0.114 * px.b as f32) as u8;
        let gray_px = bmp::Pixel {
            r: gray_color,
            g: gray_color,
            b: gray_color,
        };

        img.set_pixel(x, y, gray_px);
    }
    let _ = img.save("gray_parrots.bmp").unwrap_or_else(|e| {
        panic!("Failed to save: {}", e);
    });
}
