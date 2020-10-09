<script lang="ts">
    import { onMount, onDestroy } from 'svelte';
    import {Howl} from 'howler';
    import Paper from './elements/Paper.svelte';
    import Player from './elements/Player.svelte';
    import Enemy from './elements/Enemy.svelte';

    import type { EnemyModel } from '../utils/models';

    let rMousePress:boolean = false;

    const sounds:Howl[] = [];
    const spells:any[] = [];
    const enemies:EnemyModel[] = [
        {name: 'Goblin', hp: 200, time: 20, image: 'assets/images/goblin.png'},
        {name: 'Dwarf', hp: 350, time: 30, image: 'assets/images/dwarf.png'},
        {name: 'Dragon', hp: 500, time: 40, image: 'assets/images/dragon.png'},
        {name: 'Gilgamesh', hp: 750, time: 50, image: 'assets/images/Almighty_Gilgamesh.gif'},
        {name: 'Altes Besta', hp: 1000, time: 60, image: 'assets/images/Altes_Besta.png'},
    ];
    const colors:string[] = ['red', 'white', 'green', 'blue', 'yellow'];

    export let currentEnemy:number = 0;
    export let currentSpell:number = 0;
    export let currentColor:number = 0;

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
        playSound('nggyu');
    });

    onDestroy(():void => {
        sounds.forEach(sound => {
            sound.stop();
        });
    });

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
<div id="game">
    <Player bind:currentEnemy bind:currentSpell playSound={playSound} length={enemies.length}/>
    <Paper bind:rMousePress bind:currentColor colors={colors} />
    <Enemy enemy={enemies[currentEnemy%enemies.length]}/>
</div>

<style type="text/scss">
    #game{
        width: 100%;
        height: calc(100% - 30px);
        display: flex;
        margin: 15px 0;
    }
    #game:first-child{
        margin-left: 15px;
    }
    #game:last-child{
        margin-right: 15px;
    }
    .toolbar{
        white-space: nowrap;
        margin-right: 10px;
    }
</style>