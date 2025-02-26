{
	"targets": [
		{
	        "target_name": "node-rpi-rgb-led-matrix",
	        "sources": [ "src/base.cc", "src/ledmatrix.cc", "src/image.cc" ],
	        "dependencies": [ "./binding.gyp:rpi-rgb-led-matrix" ],
	        "include_dirs": [ "./external/matrix/include", "./external/matrix/lib", "./include/", "<!(node -e \"require('nan')\")" ]
	    },
		{
			"target_name": "rpi-rgb-led-matrix",
			"type": "static_library",
			"sources": [

			"./external/matrix/lib/thread.cc",
			"./external/matrix/lib/pixel-mapper.cc",
			"./external/matrix/lib/options-initialize.cc",
			"./external/matrix/lib/multiplex-mappers.cc",
			"./external/matrix/lib/led-matrix-c.cc",
			"./external/matrix/lib/led-matrix.cc",
			"./external/matrix/lib/graphics.cc",
			"./external/matrix/lib/gpio.cc",
			"./external/matrix/lib/framebuffer.cc",
			"./external/matrix/lib/content-streamer.cc",
			"./external/matrix/lib/bdf-font.cc",
			"./external/matrix/lib/hardware-mapping.c",

			],
			"defines": [ 
			"DFIXED_FRAME_MICROSECONDS=8500",
			],

			"libraries": ["-lrt", "-lm", "-lpthread"],
			"include_dirs": [ "external/matrix/include", "external/matrix/lib" ],
	        "direct_dependent_settings": {
	            "include_dirs": [ "external/matrix/include" ]
	        }

		}
	]
}
