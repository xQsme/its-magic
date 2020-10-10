<script lang="ts">
    export let enemy:Enemy;
</script>

<div class="container">
    <h1>{enemy.name}</h1>
    <div class="stats">
        <div class="health">
            <span>HP: {enemy.currentHP}/{enemy.hp}</span>
            <div class="progress-container">
                <div class="progress" style="width: {enemy.currentHP/enemy.hp*100}%;" />
                <span class="progress-text">{(enemy.currentHP/enemy.hp*100).toFixed(2)}%</span>
            </div>
        </div>
        <div class="mana">
            <span>MP: {enemy.time}/{enemy.time}</span>
            <div class="progress-container">
                <div class="progress" style="width: {enemy.time/enemy.time*100}%;" />
                <span class="progress-text">{(enemy.time/enemy.time*100).toFixed(2)}%</span>
            </div>
        </div>
    </div>
    <div class="enemy-container">
        <img class="enemy" src={enemy.image} alt="enemy"/>
    </div> 
</div>
     
<style lang="scss">
    .container{
        display: flex;
        background-color: #303030;
        flex-direction: column;
        flex: 1 1 auto;
        padding: 20px;

        h1{
            text-align: center;
        }

        .health{
            color: red;
            margin-bottom: 10px;

            .progress{
                background-color: red;
            }
        }

        .mana{
            color: cornflowerblue;

            .progress{
                background-color: cornflowerblue;
            }
        }

        .progress-container{
            width: 100%;
            height: 20px;
            position: relative;

            .progress{
                height: 100%;
                border-radius: 10px;
                transition: width 0.5s;
            }

            .progress-text{
                color: white;
                position: absolute;
                top: 0;
                right: 50%;
                transform: translate(50%);
            }

            .progress-placeholder{
                height: 100%;
                width: 100%;
                border-radius: 10px;
                background-color: #222222;
                margin-bottom: -20px;
            }
        }

        .enemy-container{
            display: flex;
            justify-content: center;
            align-items: center;      
            height: 100%;  
            
            .enemy{
                max-width: 25vw;
            }
        }
    }


    

</style>