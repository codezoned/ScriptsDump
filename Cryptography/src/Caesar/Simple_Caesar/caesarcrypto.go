package crypto

import (
	"strings"
)

// CaesarCipherEncode ...
func CaesarCipherEncode(input string, shift int) string {
	var output strings.Builder
	for _, c := range input {
		var lowercaseFlag bool
		if c >= 97 && c <= 122 {
			c -= 32
			lowercaseFlag = true
		}
		if c >= 65 && c <= 90 {
			c += rune(shift)
			if c > 90 {
				c = 65 + (c-90-1)%26
			} else if c < 65 {
				c = 90 - (65-c-1)%26
			}
		}
		if lowercaseFlag {
			c += 32
		}
		output.WriteRune(c)
	}
	return output.String()
}

// CaesarCipherDecode ...
func CaesarCipherDecode(input string, shift int) string {
	return CaesarCipherEncode(input, -shift)
}
