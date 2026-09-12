// Encodes PNG screenshots to AVIF next to the source, via ImageIO (no third-party tools).
// Usage: swift tools/avif.swift assets/ohayo-network/en/popover.png ...
import Foundation
import ImageIO

let quality = 0.82
for path in CommandLine.arguments.dropFirst() {
    let src = URL(fileURLWithPath: path)
    let dst = src.deletingPathExtension().appendingPathExtension("avif")
    guard let source = CGImageSourceCreateWithURL(src as CFURL, nil),
          let image = CGImageSourceCreateImageAtIndex(source, 0, nil),
          let dest = CGImageDestinationCreateWithURL(dst as CFURL, "public.avif" as CFString, 1, nil)
    else { FileHandle.standardError.write("skip \(path)\n".data(using: .utf8)!); continue }
    CGImageDestinationAddImage(dest, image, [kCGImageDestinationLossyCompressionQuality: quality] as CFDictionary)
    guard CGImageDestinationFinalize(dest) else { FileHandle.standardError.write("fail \(path)\n".data(using: .utf8)!); continue }
    let a = (try? FileManager.default.attributesOfItem(atPath: src.path)[.size] as? Int) ?? 0
    let b = (try? FileManager.default.attributesOfItem(atPath: dst.path)[.size] as? Int) ?? 0
    print("\(dst.path): \(a / 1024) KB -> \(b / 1024) KB")
}
