<script lang="ts">
    import axios from "axios";
    import { createEventDispatcher } from 'svelte'
    import { onMount, onDestroy } from 'svelte';
    import {Howl} from 'howler';
    import Paper from './elements/Paper.svelte';
    import Player from './elements/Player.svelte';
    import Enemy from './elements/Enemy.svelte';

    import type { EnemyModel, SpellModel, PlayerModel } from '../utils/models';
    import { url } from '../utils/server';

    
    
    let rMousePress:boolean = false;
    let changing:boolean = false;
    export let started:boolean = false;
    export let lost:boolean = false;
    export let currentEnemy:number = 0;
    export let currentSpell:number = 0;
    export let currentColor:number = 0;

    const dispatch = createEventDispatcher()

    const sounds:Howl[] = [];
    const spells:SpellModel[] = [
        {name: '1', image: 'assets/images/spell1.png'},
        {name: '2', image: 'assets/images/spell2.png'},
        {name: '3', image: 'assets/images/spell3.png'},
        {name: '4', image: 'assets/images/spell4.png'},
        {name: '5', image: 'assets/images/spell5.png'},
    ];
    let enemies:EnemyModel[] = [];
    const colors:string[] = ['red', 'white', 'green', 'blue', 'yellow'];
    let player:PlayerModel;
    restartGame();

    function restartGame() {
        enemies = [
            {name: 'Goblin', hp: 200, currentHP: 200, mana: 40, currentMana: 0, damage: 50, image: 'assets/images/goblin.png'},
            {name: 'Dwarf', hp: 350, currentHP: 350, mana: 40, currentMana: 0, damage: 100, image: 'assets/images/dwarf.png'},
            {name: 'Dragon', hp: 500, currentHP: 500, mana: 60, currentMana: 0, damage: 150, image: 'assets/images/dragon.png'},
            {name: 'Gilgamesh', hp: 750, currentHP: 750, mana: 75, currentMana: 0, damage: 250, image: 'assets/images/Almighty_Gilgamesh.gif'},
            {name: 'Altes Besta', hp: 1000, currentHP: 1000, mana: 80, currentMana: 0, damage: 9991, image: 'assets/images/Altes_Besta.png'},
        ];
        player = {name: 'Altes Besta', hp: 1000, currentHP: 1000, mana: 100, currentMana: 0};
        currentColor=0;
        currentEnemy=0;
        currentSpell=0;
    }

    function changeEnemy():void {
        enemies[currentEnemy%enemies.length].currentHP=enemies[currentEnemy%enemies.length].hp;
        currentEnemy++;
        if(currentEnemy%enemies.length === 4) {
            playSound('tuturu');
        }
    }

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
        //playSound('nggyu');
    });

    onDestroy(():void => {
        sounds.forEach(sound => {
            sound.stop();
        });
    });

    function dealDamageToPlayer() {
        player.currentHP -= enemies[currentEnemy%enemies.length].damage;
        if(player.currentHP <= 0) {
            player.currentHP = 0;
            started=false;
            lost=true;
        }
    }

    function submitSpell(spell){
        axios({
            method: 'post',
            url: url + 'spell',
            headers: {
                'Content-Type' : 'application/json',
            },
            data: {
                spell: spell
            }
        }).then(response=>{
            console.log(response);
            
        })
        .catch(error=>{
            console.log(error);
            
        });       
        spellActivation()
    }

    function spellActivation(){
        dispatch("spellActivation");     
        
        /*enemies[currentEnemy%enemies.length].currentHP -= 100;
        if(enemies[currentEnemy%enemies.length].currentHP <= 0) {
            enemies[currentEnemy%enemies.length].currentHP = 0;
            changing = true;
            setTimeout(() => {
                changeEnemy();
                changing=false;
            }, 500);
        }
        player.currentMana += 10;
        if(player.currentMana >= player.mana) {   
            player.currentMana = player.mana;
        }*/
    }

    function special() {
        player.currentMana=0;
        enemies[currentEnemy%enemies.length].currentHP -= 250;
        if(enemies[currentEnemy%enemies.length].currentHP <= 0) {
            enemies[currentEnemy%enemies.length].currentHP = 0;
            setTimeout(() => {
                changeEnemy();
            }, 500);
        }
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
<div id="game">
    <Player player={player}/>
    <Paper bind:rMousePress bind:currentColor colors={colors} bind:currentSpell spells={spells} submitSpell={submitSpell} player={player} special={special} changing={changing} bind:started lost={lost} restartGame={restartGame} />
    <Enemy enemy={enemies[currentEnemy%enemies.length]} dealDamageToPlayer={dealDamageToPlayer} started={started} on:spellActivation={spellActivation}/>
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