REF_NODES_ARRAY = [
  {
    "id": 1000000001,
    "shape": "image",
    "size": 10,
    "fixed": {
      "x": true,
      "y": true
    },
    "image": "./refs/gray.png",
    "title": "./refs/gray.png\nHSV:0,0,76",
    "x": 0.0,
    "y": 0.0
  },
  {
    "id": 1000000002,
    "shape": "image",
    "size": 10,
    "fixed": {
      "x": true,
      "y": true
    },
    "image": "./refs/red.png",
    "title": "./refs/red.png\nHSV:0,100,100",
    "x": 3.061616997868383e-14,
    "y": -500.0
  },
  {
    "id": 1000000003,
    "shape": "image",
    "size": 10,
    "fixed": {
      "x": true,
      "y": true
    },
    "image": "./refs/yellow.png",
    "title": "./refs/yellow.png\nHSV:60,100,100",
    "x": 433.0127018922194,
    "y": -249.99999999999997
  },
  {
    "id": 1000000004,
    "shape": "image",
    "size": 10,
    "fixed": {
      "x": true,
      "y": true
    },
    "image": "./refs/green.png",
    "title": "./refs/green.png\nHSV:120,100,100",
    "x": 433.0127018922194,
    "y": 249.99999999999997
  },
  {
    "id": 1000000005,
    "shape": "image",
    "size": 10,
    "fixed": {
      "x": true,
      "y": true
    },
    "image": "./refs/cyan.png",
    "title": "./refs/cyan.png\nHSV:180,100,100",
    "x": 3.061616997868383e-14,
    "y": 500.0
  },
  {
    "id": 1000000006,
    "shape": "image",
    "size": 10,
    "fixed": {
      "x": true,
      "y": true
    },
    "image": "./refs/blue.png",
    "title": "./refs/blue.png\nHSV:240,100,100",
    "x": -433.0127018922194,
    "y": 249.99999999999997
  },
  {
    "id": 1000000007,
    "shape": "image",
    "size": 10,
    "fixed": {
      "x": true,
      "y": true
    },
    "image": "./refs/magenta.png",
    "title": "./refs/magenta.png\nHSV:300,100,100",
    "x": -433.0127018922193,
    "y": -250.00000000000006
  },
];
REF_EDGES_ARRAY = [
  {from: 1000000001, to: 1000000002, smooth:false, color: 'red' },
  {from: 1000000001, to: 1000000003, smooth:false, color: 'yellow' },
  {from: 1000000001, to: 1000000004, smooth:false, color: 'green' },
  {from: 1000000001, to: 1000000005, smooth:false, color: 'cyan' },
  {from: 1000000001, to: 1000000006, smooth:false, color: 'blue' },
  {from: 1000000001, to: 1000000007, smooth:false, color: 'magenta' },
  {from: 1000000002, to: 1000000003, smooth:false, color: 'white' },
  {from: 1000000003, to: 1000000004, smooth:false, color: 'white' },
  {from: 1000000004, to: 1000000005, smooth:false, color: 'white' },
  {from: 1000000005, to: 1000000006, smooth:false, color: 'white' },
  {from: 1000000006, to: 1000000007, smooth:false, color: 'white' },
  {from: 1000000007, to: 1000000002, smooth:false, color: 'white' }
];