CREATE OR REPLACE FUNCTION init_tables()
	returns void
	language sql
	as $$

	create table if not exists "Lounge_bars" (
		id serial not null primary key,
		name text not null,
		address text not null,
		supplier text not null,
		owner text not null,
		common_tobacco text not null
		);

	create table if not exists "Suppliers" (
		organisation text not null primary key,
		volume_purchase_per_month numeric(8,2) not null,
		phone_number varchar(11) not null
		);

	create table if not exists "Owners" (
		name text not null primary key,
		foundation_date date not null,
		email text not null
		);

	create table if not exists "Ratings" (
		lounge_bar_name text not null,
		feedback text not null,
		grade integer not null
		);


	create index if not exists name on "Lounge_bars" (name);
	create index if not exists owner on "Owners" (email);
	create index if not exists supplier on "Suppliers" (phone_number);

    create or replace function update_supplier()
		 returns trigger as $u1$
		begin
		   if old.organisation != new.organisation then
			update "Lounge_bars" set supplier = new.organisation
			where supplier = old.organisation;
		   end if;
		   return new;
		end;
		 $u1$ language plpgsql;

	drop trigger if exists trigger_supplier on "Suppliers";
	create trigger trigger_supplier after update on "Suppliers"
	   for row execute procedure update_supplier();

	create or replace function update_owner()
		returns trigger as  $u2$
		begin
		   if old.name != new.name then
			update "Lounge_bars" set owner = new.name
			where owner = old.name;
		   end if;
		   return new;
		end;
		$u2$ language plpgsql;

	drop trigger if exists trigger_owner on "Owners";
	create trigger trigger_owner after update on "Owners"
	   for row execute procedure update_owner();


	create or replace function update_lounge_bar()
		returns trigger as $u3$
		begin
		   if old.name != new.name then
			update "Ratings" set lounge_bar_name = new.name
			where lounge_bar_name = old.name;
		   end if;
		   return new;
		end;
		$u3$ language plpgsql;

	drop trigger if exists trigger_lounge_bar on "Lounge_bars";
	create trigger trigger_lounge_bar after update on "Lounge_bars"
	   for row execute procedure update_lounge_bar();
$$;