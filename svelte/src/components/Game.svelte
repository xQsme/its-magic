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
    export let currentXP:number = 0;
    export let enemyDamage:any[] = [];
    export let playerDamage:any[] = [];
    export let playerXP:any[] = [];
    export let levelUp:boolean = false;

    const sounds:Howl[] = [];
    let spells:SpellModel[] = [];
    let enemies:EnemyModel[] = [];
    let colors:ColorModel[] = [];
    let players:PlayerModel[] = [];
    let player:PlayerModel;
    restartGame();

    function restartGame() {
        sounds.forEach(sound => {
            sound.stop();
        });
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
        axios.get(url + 'player/').then(result => {
            for(let i = 0; i < result.data.length; i++) {
                result.data[i].currentHP = result.data[i].hp;
                if(result.data[i].mana <= 0) {
                    result.data[i].mana = 10;
                }
            }
            players = result.data;
            player = players[0];
        });
        currentColor=0;
        currentEnemy=0;
        currentSpell=0;

        randomizeSpells();

        if(enemies.length > 0) {
            playSound(enemies[currentEnemy%enemies.length].sound);
        }
        if(players.length > 0) {
            playSound(player.sound);
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
        const value = Math.floor(enemies[currentEnemy%enemies.length].damage * (Math.random() + 0.5));
        const damage = {value, random: Math.random()*90};
        playerDamage.push(damage);
        setTimeout(() => playerDamage.splice(playerDamage.indexOf(damage), 1), 2000);
        player.currentHP -= value;
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
        randomizeSpells();
    }

    function randomizeSpells() {
        if(spells.length > 2) {
            const nextSpell = spells[(currentSpell)%spells.length];
            const nextNextSpell = spells[(currentSpell+1)%spells.length];
            let i;
            let j;
            do{
                shuffle(spells);
                i = spells.indexOf(nextSpell);
                j = spells.indexOf(nextNextSpell);
            } while(i === ((currentSpell + 1)%spells.length) || j === (currentSpell%spells.length));
            let temp = spells[(currentSpell)%spells.length];
            spells[(currentSpell)%spells.length] = nextSpell;
            spells[i] = temp;
            temp = spells[(currentSpell+1)%spells.length];
            spells[(currentSpell+1)%spells.length] = nextNextSpell;
            spells[j] = temp;
        }
    }

    function shuffle(array) {
        var currentIndex = array.length, temporaryValue, randomIndex;

        // While there remain elements to shuffle...
        while (0 !== currentIndex) {

            // Pick a remaining element...
            randomIndex = Math.floor(Math.random() * currentIndex);
            currentIndex -= 1;

            // And swap it with the current element.
            temporaryValue = array[currentIndex];
            array[currentIndex] = array[randomIndex];
            array[randomIndex] = temporaryValue;
        }

        return array;
    }

    function shouldChangePlayer() {
        let sum = 0;
        let prevSum = 0;
        let prevPlayer = null;
        players.forEach(p => {
            sum += p.xp;
            if(sum > currentXP) {
                if(player.id !== p.id) {
                    player=p;
                    player.currentXP = currentXP - prevSum;
                    playSound(player.sound);
                    levelUp = true;
                    setTimeout(() => {
                        levelUp = false;
                    }, 2000);
                }
                return;
            }
            prevSum += p.xp;
            prevPlayer = p;
        });
    }

    function spellActivation(){
        const damage = {value: 100, random: Math.random()*90};
        enemyDamage.push(damage);
        setTimeout(() => enemyDamage.splice(enemyDamage.indexOf(damage), 1), 2000);
        enemies[currentEnemy%enemies.length].currentHP -= 100;
        if(enemies[currentEnemy%enemies.length].currentHP <= 0) {
            const xp = {value: enemies[currentEnemy%enemies.length].xp, random: Math.random()*90};
            currentXP += xp.value;
            playerXP.push(xp);
            setTimeout(() => playerXP.splice(playerXP.indexOf(xp), 1), 3500);
            enemies[currentEnemy%enemies.length].currentHP = 0;
            changing = true;
            setTimeout(() => {
                changeEnemy();
                changing=false;
                shouldChangePlayer();
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
    {#if enemies.length > 0 && colors.length > 0 && spells.length > 0 && players.length > 0}
        <Player damage={playerDamage} xp={playerXP} player={player} levelUp={levelUp}/>
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