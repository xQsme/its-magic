export interface AuthModel {
	email:string,
	username:string,
	role:string[],
    token:string,
}

export interface EnemyModel{
    name:string,
    hp:number,
    currentHP:number,
    mana:number,
    currentMana:number,
    damage:number,
    time:number,
    image:string,
}

export interface SpellModel{
    name:string,
    image:string,
}

export interface PlayerModel{
    name:string,
    hp:number,
    currentHP:number,
    mana:number,
    currentMana:number,
}