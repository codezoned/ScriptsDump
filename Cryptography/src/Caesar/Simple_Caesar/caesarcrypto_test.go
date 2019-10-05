package crypto

import (
	"reflect"
	"testing"
)

func Test_CaesarCipherEncode(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		shift    int
		expected string
	}{
		{
			name:     "Encode 1",
			input:    "A quIck BrOwN FoX jUMps OvEr thE lAzY DoG 123",
			shift:    3,
			expected: "D txLfn EuRzQ IrA mXPsv RyHu wkH oDcB GrJ 123",
		},
		{
			name:     "Encode 2",
			input:    "A quIck BrOwN FoX jUMps OvEr thE lAzY DoG 123",
			shift:    -3,
			expected: "X nrFzh YoLtK ClU gRJmp LsBo qeB iXwV AlD 123",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := CaesarCipherEncode(tt.input, tt.shift); !reflect.DeepEqual(got, tt.expected) {
				t.Errorf("CaesarCipherEncode() = %v, expected %v", got, tt.expected)
			}
		})
	}
}

func Test_CaesarCipherDecode(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		shift    int
		expected string
	}{
		{
			name:     "Decode 1",
			input:    "D txLfn EuRzQ IrA mXPsv RyHu wkH oDcB GrJ 123",
			shift:    3,
			expected: "A quIck BrOwN FoX jUMps OvEr thE lAzY DoG 123",
		},
		{
			name:     "Decode 2",
			input:    "X nrFzh YoLtK ClU gRJmp LsBo qeB iXwV AlD 123",
			shift:    -3,
			expected: "A quIck BrOwN FoX jUMps OvEr thE lAzY DoG 123",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := CaesarCipherDecode(tt.input, tt.shift); !reflect.DeepEqual(got, tt.expected) {
				t.Errorf("CaesarCipherDecode() = %v, expected %v", got, tt.expected)
			}
		})
	}
}
