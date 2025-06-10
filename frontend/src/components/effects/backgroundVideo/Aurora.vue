<template>
    <div ref="canvasRef" class="aurora-canvas"></div>
  </template>
  
  <script setup>
  import { ref, onMounted, onBeforeUnmount } from 'vue'
  import { Renderer, Program, Mesh, Color, Triangle, Transform } from 'ogl'
    
  // GLSL from your example:
  const VERT = `#version 300 es
  in vec2 position;
  void main() {
    gl_Position = vec4(position, 0.0, 1.0);
  }
  `
  const FRAG = `#version 300 es
precision highp float;
out vec4 fragColor;
void main() {
  fragColor = vec4(1.0, 0.0, 0.0, 1.0);  // pure red
}
`;


  
  // Props for customization:
  const props = defineProps({
    colorStops: {
      type: Array,
      default: () => ['#5227FF', '#7cff67', '#5227FF']
    },
    amplitude: { type: Number, default: 1.0 },
    blend:     { type: Number, default: 0.5 },
    speed:     { type: Number, default: 1.0 },
  })
  
  const canvasRef = ref(null)
  let renderer, program, mesh, rafId
  
  onMounted(() => {
    const container = canvasRef.value
    renderer = new Renderer({ alpha: true })
    const gl = renderer.gl
    gl.clearColor(0, 0, 0, 0)
    gl.enable(gl.BLEND)
    gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_ALPHA)
    container.appendChild(gl.canvas)
  
    // Build geometry + program
    const sceneRoot = new Transform()              // ← root node
    const geometry = new Triangle(gl)
    if (geometry.attributes.uv) delete geometry.attributes.uv
  
    // initial colorStops as vec3[]
    const stops = props.colorStops.map(h => {
      const c = new Color(h)
      return [c.r, c.g, c.b]
    })
  
    program = new Program(gl, {
      vertex:   VERT,
      fragment: FRAG,
      uniforms: {
        uTime:       { value: 0 },
        uAmplitude:  { value: props.amplitude },
        uColorStops: { value: stops },
        uResolution: { value: [container.offsetWidth, container.offsetHeight] },
        uBlend:      { value: props.blend },
      }
    })
  
// 3) Parent the mesh to the root transform
    mesh = new Mesh(gl, { geometry, program, parent: sceneRoot })
  
    // handle resize
    const resize = () => {
      const w = container.offsetWidth
      const h = container.offsetHeight
      renderer.setSize(w, h)
      program.uniforms.uResolution.value = [w, h]
    }
    window.addEventListener('resize', resize)
    resize()
  
    // render loop
    let start = performance.now()
    const update = (t) => {
      rafId = requestAnimationFrame(update)
      const elapsed = (t - start) * 0.001 * props.speed
      program.uniforms.uTime.value      = elapsed
      program.uniforms.uAmplitude.value = props.amplitude
      program.uniforms.uBlend.value     = props.blend
      // update color stops in case they change
      program.uniforms.uColorStops.value =
        props.colorStops.map(h => {
          const c = new Color(h)
          return [c.r, c.g, c.b]
        })
  
        renderer.render({ scene: sceneRoot })    }
    rafId = requestAnimationFrame(update)
  })
  
  onBeforeUnmount(() => {
    cancelAnimationFrame(rafId)
    if (renderer) {
      renderer.gl.getExtension('WEBGL_lose_context')?.loseContext()
    }
  })
  </script>
  
  <style scoped>
    .aurora-canvas {
    position: absolute;
    inset: 0;
    z-index: 999;
    /* DEBUG only: */
    /* border: 2px dashed red;
    background: rgba(255, 0, 0, 0.1); */
    }
  </style>
  