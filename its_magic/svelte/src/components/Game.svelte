<script lang="ts">
    import { onMount, onDestroy } from 'svelte';
    import * as PIXI from 'pixi.js';
    import {Howl, Howler} from 'howler';
    import Paper from './elements/Paper.svelte';
    // import paper from 'paper';

    let app:any;
    let button:any;
    let showPaper:boolean = false;
    let rMousePress:boolean = false;

    const sounds:Howl[] = [];
    const spells:any[] = [];
    const enemies:any[] = [
        {name: 'Goblin', hp: '200', time: 20, image: 'assets/images/goblin.png'},
        {name: 'Dwarf', hp: '350', time: 30, image: 'assets/images/dwarf.png'},
        {name: 'Dragon', hp: '500', time: 40, image: 'assets/images/dragon.png'},
        {name: 'Gilgamesh', hp: '750', time: 50, image: 'assets/images/Almighty_Gilgamesh.gif'},
        {name: 'Altes Besta', hp: '1000', time: 60, image: 'assets/images/Altes_Besta.png'},
    ];
    const colors:string[] = ['red', 'white', 'green', 'blue', 'yellow'];

    let currentEnemy:number = 0;
    let dude:any = null;
    let currentSpell:number = 0;
    let currentColor:number = 0;

    //Disable right click
    if(document.addEventListener) {
        document.addEventListener('contextmenu', function(e:any):void {
            rMousePress=true;
            e.preventDefault();
        }, false);
    } else {
        document.attachEvent('oncontextmenu', function():void {
            rMousePress=true;
            window.event.returnValue = false;
        });
    }

    onMount(():void => {
        const game:HTMLElement = document.getElementById('game');
        app = new PIXI.Application({ width: game.offsetWidth, height: game.offsetHeight /*resizeTo: game*/ });
        game.appendChild(app.view);

        var background = PIXI.Sprite.from('assets/images/background.png');

        background.anchor.x = 0;
        background.anchor.y = 0;

        background.position.x = 0;
        background.position.y = 0;

        background.width = app.screen.width;
        background.height = app.screen.height;

        app.stage.addChild(background);

        const textureButton:any = PIXI.Texture.from('assets/images/play.png');

        button = new PIXI.Sprite(textureButton);

        button.anchor.set(0.5);
        button.scale.set(0.1)
;       button.x = app.screen.width/2;
        button.y = app.screen.height/2;

        // make the button interactive...
        button.interactive = true;
        button.buttonMode = true;

        button.on('pointerdown', startGame);

        // Use mouse-only events
        // .on('mousedown', onButtonDown)
        // .on('mouseup', onButtonUp)
        // .on('mouseupoutside', onButtonUp)
        // .on('mouseover', onButtonOver)
        // .on('mouseout', onButtonOut)

        // Use touch-only events
        // .on('touchstart', onButtonDown)
        // .on('touchend', onButtonUp)
        // .on('touchendoutside', onButtonUp)

        // add it to the stage
        app.stage.addChild(button);
    });

    onDestroy(():void => {
        sounds.forEach(sound => {
            sound.stop();
        });
    });

    function changeEnemy():void {
        if(showPaper) {
            clearEnemy();
            currentEnemy++;
            if(currentEnemy%enemies.length === 4) {
                playSound('tuturu');
            }
            addEnemy();
        }
    }

    function addEnemy():void {
        dude = PIXI.Sprite.from(enemies[currentEnemy%enemies.length].image);
        dude.anchor.set(0.5);
        dude.x = app.screen.width*3/4;
        dude.y = app.screen.height/2;
        app.stage.addChild(dude);
    }

    function clearEnemy():void {
        app.stage.removeChild(dude)
    }

    function startGame():void {
        app.stage.removeChild(button);

        showPaper = true;

        addEnemy();

        // const aliens:any[] = [];

        // const totalDudes:number = 10;
        // const sexydudes:string[] = [];

        // //Adding some diversity
        // sexydudes.push('assets/images/Almighty_Gilgamesh.gif');
        // sexydudes.push('assets/images/Almighty_Sanchez.png');
        // sexydudes.push('assets/images/Altes_Besta.png');
        // sexydudes.push('assets/images/Almighty_Just_Right.png');
        
        // for (var i = 0; i < totalDudes-4; i++) {
        // 	sexydudes.push('assets/images/rick.jpg');
        // }
        // console.log("Give me that mustache e faço add")


        // for (let i = 0; i < totalDudes ; i++) {
        //     // create a new Sprite that uses the image name that we just generated as its source
        //     const dude:any = PIXI.Sprite.from(sexydudes[i]);

        //     // set the anchor point so the texture is centerd on the sprite
        //     dude.anchor.set(0.5);

        //     // set a random scale for the dude - no point them all being the same size!
        //     dude.scale.set(0.2 + Math.random() * 0.3);

        //     // finally lets set the dude to be at a random position..
        //     dude.x = Math.random() * app.screen.width;
        //     dude.y = Math.random() * app.screen.height;

        //     dude.tint = Math.random() * 0xFFFFFF;

        //     // create some extra properties that will control movement :
        //     // create a random direction in radians. This is a number between 0 and PI*2 which is the equivalent of 0 - 360 degrees
        //     dude.direction = Math.random() * Math.PI * 2;

        //     // this number will be used to modify the direction of the dude over time
        //     dude.turningSpeed = Math.random() - 0.8;

        //     // create a random speed for the dude between 2 - 4
        //     dude.speed = 2 + Math.random() * 2;

        //     // finally we push the dude into the aliens array so it it can be easily accessed later
        //     aliens.push(dude);

        //     app.stage.addChild(dude);
        // }

        // // create a bounding box for the little dudes
        // const dudeBoundsPadding:number = 100;
        // const dudeBounds:any = new PIXI.Rectangle(-dudeBoundsPadding,
        //     -dudeBoundsPadding,
        //     app.screen.width + dudeBoundsPadding * 2,
        //     app.screen.height + dudeBoundsPadding * 2);

        // app.ticker.add(() => {
        //     // iterate through the dudes and update their position
        //     for (let i = 0; i < aliens.length; i++) {
        //         const dude = aliens[i];
        //         dude.direction += dude.turningSpeed * 0.01;
        //         dude.x += Math.sin(dude.direction) * dude.speed;
        //         dude.y += Math.cos(dude.direction) * dude.speed;
        //         dude.rotation = -dude.direction - Math.PI / 2;

        //         // wrap the dudes by testing their bounds...
        //         if (dude.x < dudeBounds.x) {
        //             dude.x += dudeBounds.width;
        //         } else if (dude.x > dudeBounds.x + dudeBounds.width) {
        //             dude.x -= dudeBounds.width;
        //         }

        //         if (dude.y < dudeBounds.y) {
        //             dude.y += dudeBounds.height;
        //         } else if (dude.y > dudeBounds.y + dudeBounds.height) {
        //             dude.y -= dudeBounds.height;
        //         }
        //     }
        // });

        //Podem dar mute na tab do browser, nao comentem isto xD
        playSound('tuturu');
    }

    function playSound(file) {
        var sound:any = new Howl({
            src: ['assets/sounds/' + file + '.mp3']
        });
        sounds.push(sound);
        sound.on('end', () => {
            sounds.splice(sounds.indexOf(sound), 1);
        });
        sound.play();
    }
</script>

<div class="toolbar">
    <p>Current Enemy: {currentEnemy}</p>
    <button on:click={changeEnemy}>Next Enemy</button>

    <p>Current Spell: {currentSpell}</p>
    <button on:click={() => currentSpell++}>Next Spell</button>

    <p>Current Color: {currentColor}</p>
    <button on:click={() => currentColor++}>Next Color</button>
</div>
<div id="game">
    <Paper showPaper={showPaper} bind:rMousePress currentColor={colors[currentColor%colors.length]} />
</div>

<style type="text/scss">
    #game{
        width: 100%;
        height: 100%;
    }
    .toolbar{
        white-space: nowrap;
        margin-right: 10px;
    }
</style>