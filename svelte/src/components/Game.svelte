<script lang="ts">
    import axios from "axios";
    import { onMount, onDestroy } from 'svelte';
    import {Howl} from 'howler';
    import Paper from './elements/Paper.svelte';
    import Player from './elements/Player.svelte';
    import Enemy from './elements/Enemy.svelte';

    import type { EnemyModel, SpellModel, PlayerModel, ColorModel } from '../utils/models';
    import { url } from '../utils/server';
    
    let rMousePress:boolean = false;
    let changing:boolean = false;
    export let started:boolean = false;
    export let lost:boolean = false;
    export let currentEnemy:number = 0;
    export let currentSpell:number = 0;
    export let currentColor:number = 0;
    export let enemyDamage:any[] = [];
    export let playerDamage:any[] = [];

    const sounds:Howl[] = [];
    let spells:SpellModel[] = [];
    let enemies:EnemyModel[] = [];
    let colors:ColorModel[] = [];
    let player:PlayerModel;
    restartGame();

    function restartGame() {
        axios.get(url + 'enemy/').then(result => {
            for(let i = 0; i < result.data.length; i++) {
                result.data[i].currentHP = result.data[i].hp;
                if(result.data[i].mana <= 0) {
                    result.data[i].mana = 10;
                }
            }
            enemies = result.data;
        });
        axios.get(url + 'color/').then(result => {
            colors = result.data;
        });
        axios.get(url + 'spell/').then(result => {
            spells = result.data;
        });
        player = {name: 'Altes Besta', hp: 1000, currentHP: 1000, mana: 100, currentMana: 0};
        currentColor=0;
        currentEnemy=0;
        currentSpell=0;
        if(enemies.length > 0) {
            playSound(enemies[currentEnemy%enemies.length].sound);
        }
    }

    function changeEnemy():void {
        sounds.forEach(sound => {
            sound.stop();
        });
        enemies[currentEnemy%enemies.length].currentHP=enemies[currentEnemy%enemies.length].hp;
        currentEnemy++;
        playSound(enemies[currentEnemy%enemies.length].sound);
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
        const damage = {value: enemies[currentEnemy%enemies.length].damage, random: Math.random()*90};
        playerDamage.push(damage);
        setTimeout(() => playerDamage.splice(playerDamage.indexOf(damage), 1), 2000);
        player.currentHP -= enemies[currentEnemy%enemies.length].damage;
        if(player.currentHP <= 0) {
            player.currentHP = 0;
            started=false;
            lost=true;
        }
    }

    function submitSpell(spell){
        /*axios({
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
            
        });*/       
        spellActivation();
    }

    function spellActivation(){
        const damage = {value: 100, random: Math.random()*90};
        enemyDamage.push(damage);
        setTimeout(() => enemyDamage.splice(enemyDamage.indexOf(damage), 1), 2000);
        enemies[currentEnemy%enemies.length].currentHP -= 100;
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
        }
    }

    function special() {
        const damage = {value: 250, random: Math.random()*90};
        enemyDamage.push(damage);
        setTimeout(() => enemyDamage.splice(enemyDamage.indexOf(damage), 1), 2000);
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
            src: [file]
        });
        sounds.push(sound);
        sound.on('end', () => {
            sounds.splice(sounds.indexOf(sound), 1);
        });
        sound.play();
    }
</script>
<div id="game">
    {#if enemies.length > 0 && colors.length > 0 && spells.length > 0}
        <Player damage={playerDamage} player={player}/>
        <Paper bind:rMousePress bind:currentColor colors={colors} bind:currentSpell spells={spells} submitSpell={submitSpell} player={player} special={special} changing={changing} bind:started lost={lost} restartGame={restartGame} />
        <Enemy damage={enemyDamage} enemy={enemies[currentEnemy%enemies.length]} dealDamageToPlayer={dealDamageToPlayer} started={started} on:activation={() => (console.log("fine i will close myself"))}/>
    {:else}
        <h1>Not enough assets to run the game, please contact an administrator.</h1>
    {/if}
</div>

<style type="text/scss">
    #game{
        width: 100%;
        height: calc(100% - 30px);
        display: flex;
        margin: 15px 0;

        h1{
            text-align: center;
            width: 100%;
        }
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