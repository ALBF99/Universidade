function init(mesh) {
    var renderer = new THREE.WebGLRenderer();
    renderer.setSize( window.innerWidth, window.innerHeight );

    renderer.setClearColor("grey");
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    renderer.setPixelRatio(window.devicePixelRatio * 2);
    document.body.appendChild(renderer.domElement);

    var camera = new THREE.PerspectiveCamera( 120, window.innerWidth/window.innerHeight, 1, 1000 );

    var controls = new THREE.OrbitControls(camera);

    camera.position.set(-35, 14, -12);

    controls.update();

    var scene = new THREE.Scene();

    var ambientLight = new THREE.AmbientLight("#ffffff", 0.7);
    scene.add(ambientLight);

    var lighpoint = new THREE.PointLight("#ffffff", 0.5);
    lighpoint.position.set(-100, 400, 0);
    scene.add(lighpoint);

    var spotLight = new THREE.DirectionalLight("#ffffff", 0.5);
    spotLight.position.set(-200, 190, 40);
    spotLight.castShadow = true;
    spotLight.shadow.camera.near = 100;
    spotLight.shadow.camera.left = 20;
    spotLight.shadow.camera.top = 18;
    spotLight.shadow.camera.bottom = -20;
    spotLight.shadow.camera.right = -10;

    scene.add(spotLight);
    
    var helper = new THREE.CameraHelper(camera);
    scene.add(helper);

    var geo_chao = new THREE.PlaneBufferGeometry(10000, 2000, 20, 20);
    var material_chao = new THREE.MeshPhysicalMaterial({
        color: "#ffffff",
    });
    var chao = new THREE.Mesh(geo_chao, material_chao);
    chao.receiveShadow = true;
    chao.rotation.x = -1.56;
    chao.position.y = -16;
    scene.add(chao);

    scene.add(mesh.mesa);
    renderer.render(scene, camera);

    return {
        camera: camera,
        scene: scene,
        renderer: renderer,
        controls: controls,
        mesh: mesh,
    }
}

function pernas() {
    var geo_perna = new THREE.BoxGeometry(2, 38.5, 2);
    var material_perna = new THREE.MeshPhongMaterial( { color: "#efece3" } );
    var perna = new THREE.Mesh( geo_perna, material_perna );
    perna.receiveShadow = true;
    perna.castShadow = true;

    return perna;
}

function base_gaveta() {
    var geo_base = new THREE.BoxGeometry(42, 7, 47);
    var material_base = new THREE.MeshPhongMaterial( { color: "#efece3" } );
    var baseGaveta = new THREE.Mesh(geo_base, material_base);
    baseGaveta.receiveShadow = true;
    baseGaveta.castShadow = true;

    return baseGaveta;
} 

function detalhes_madeira(){
    var geo_detalhe = new THREE.BoxGeometry(42, 1, 47);
    var loader = new THREE.TextureLoader();
    var diffuseMap = loader.load("media/light_wood.jpg");
    var material_detalhe = new THREE.MeshPhongMaterial({
        color: 0xFFFFFF,
        specular: 0xffffff,
        map: diffuseMap,
    });
    var detalhe = new THREE.Mesh(geo_detalhe, material_detalhe);
    detalhe.receiveShadow = true;
    detalhe.castShadow = true;

    return detalhe;
}

function tampos(){
    var geo_tampo = new THREE.BoxGeometry(41.9, 1, 46.9);
    var material_tampo = new THREE.MeshBasicMaterial( { 
        color:"#efece3", 
        side: THREE.DoubleSide
    });
    var tampo = new THREE.Mesh( geo_tampo, material_tampo);
    tampo.receiveShadow = true;
    tampo.castShadow = true;

    return tampo;
}

function puxadores(){
    var geo_pux = new THREE.BoxGeometry(1.5, 1, 6);
    var loader = new THREE.TextureLoader();
    var diffuseMap = loader.load("media/metal.jpg");
    var material_pux = new THREE.MeshPhongMaterial({
        color: 0xFFFFFF,
        specular: 0xffffff,
        map: diffuseMap,
    });
    var puxador = new THREE.Mesh(geo_pux, material_pux);
    puxador.receiveShadow = true;
    puxador.castShadow = true;

    return puxador;
}

function prateleira() {
    var geo_prat = new THREE.BoxGeometry(38, 0.5, 43);
    var material_prat = new THREE.MeshPhongMaterial( { color: "#efece3" } );
    var prateleira = new THREE.Mesh(geo_prat, material_prat);
    prateleira.receiveShadow = true;
    prateleira.castShadow = true;

    return prateleira;
}

function suporte_pernas() {
    var geo_suporte = new THREE.BoxGeometry(40, 2, 2);
    var material_suporte = new THREE.MeshPhongMaterial( { color: "#efece3" } );
    var suporte = new THREE.Mesh(geo_suporte, material_suporte);
    suporte.receiveShadow = true;
    suporte.castShadow = true;

    return suporte;
}

function componentes() {
    var perna_esq_frente = pernas();
    perna_esq_frente.position.set(0, 13.3, 0);

    var perna_dir_frente = pernas();
    perna_dir_frente.position.set(0, 13.3, 45);

    var perna_esq_tras = pernas();
    perna_esq_tras.position.set(40, 13.3, 45);

    var perna_dir_tras = pernas();
    perna_dir_tras.position.set(40, 13.3, 0);

    var baseGaveta = base_gaveta();
    baseGaveta.position.set(20, 37, 22.5);

    var detalhe1 = detalhes_madeira();
    detalhe1.position.set(20, 41, 22.5);

    var detalhe2 = detalhes_madeira();
    detalhe2.position.set(20, 33, 22.5);

    var tampo_cima = tampos();
    tampo_cima.position.set(20, 41.1, 22.5);

    var tampo_baixo = tampos();
    tampo_baixo.position.set(20, 32.9, 22.5);

    var puxador = puxadores();
    puxador.position.set(-1, 39, 22.5);

    var prateleira1 = prateleira();
    prateleira1.position.set(20, 12, 22.5);

    var suporte_esq = suporte_pernas();
    suporte_esq.position.set(20, -3.5, 0);

    var suporte_dir = suporte_pernas();
    suporte_dir.position.set(20, -3.5, 45);

    var mesa = new THREE.Object3D();
    mesa.add(perna_esq_frente);
    mesa.add(perna_dir_frente);
    mesa.add(perna_esq_tras);
    mesa.add(perna_dir_tras);
    mesa.add(baseGaveta);
    mesa.add(detalhe1);
    mesa.add(detalhe2);
    mesa.add(tampo_cima);
    mesa.add(tampo_baixo);
    mesa.add(puxador);
    mesa.add(prateleira1);
    mesa.add(suporte_esq);
    mesa.add(suporte_dir);

    mesa.position.y = -10;

    return {
        mesa: mesa,
        prateleira1: prateleira1,
        perna_esq_frente: perna_esq_frente,
        perna_dir_frente: perna_dir_frente,
        perna_esq_tras: perna_esq_tras,
        perna_dir_tras: perna_dir_tras,
        baseGaveta: baseGaveta,
        detalhe1: detalhe1,
        detalhe2: detalhe2,
        tampo_cima: tampo_cima,
        tampo_baixo: tampo_baixo,
        puxador: puxador,
        suporte_esq: suporte_esq,
        suporte_dir: suporte_dir,
    }
}

function animate(step) {
    requestAnimationFrame(function () {
        animate(step);
    });
    step.controls.update();
    step.renderer.render(step.scene, step.camera);
}

function main(){
    var step = init(componentes());
    animate(step);
}

main();