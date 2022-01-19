/*----------------------Ratings-------------------*/

create or replace function add_rating(in lounge_bar_name text, in feedback text, in grade integer)
	returns void
	language sql
	as $$

	insert into "Ratings" (lounge_bar_name, feedback, grade)
    values (lounge_bar_name, feedback, grade)

$$;

create or replace function get_ratings()
	returns json
	language plpgsql
	as $$
		begin
		   return (select json_agg(json_build_object(
				'lounge_bar_name', "Ratings".lounge_bar_name,
				'feedback', "Ratings".feedback,
				'grade', "Ratings".grade)) from "Ratings");
		end
$$;

create or replace function delete_ratings()
	returns void
	language sql
	as $$

	truncate "Ratings"

$$;
/*------------------------------------------------*/


/*------------------------------Suppliers--------------------------*/

create or replace function add_supplier(in organisation text, in volume_purchase_per_month numeric(8,2), in phone_number varchar(11))
	returns void
	language sql
	as $$

	insert into "Suppliers" (organisation,volume_purchase_per_month,phone_number)
    values (organisation, volume_purchase_per_month, phone_number)

$$;

create or replace function delete_supplier(in organisation0 text)
	returns void
	language sql
	as $$

	delete from "Suppliers" where organisation = organisation0

$$;

create or replace function get_suppliers()
	returns json
	language plpgsql
	as $$
		begin
		   return (select json_agg(json_build_object(
				'organisation', "Suppliers".organisation,
				'volume_purchase_per_month', "Suppliers".volume_purchase_per_month,
				'phone_number', "Suppliers".phone_number)) from "Suppliers");
		end
	$$;

create or replace function delete_suppliers()
	returns void
	language sql
	as $$

	truncate "Suppliers"

$$;

create or replace function search_supplier(in phone_number0 varchar(11))
	returns json
	language plpgsql
	as $$
		begin
		   return (select json_agg(json_build_object(
				'organisation', "Suppliers".organisation,
				'volume_purchase_per_month', "Suppliers".volume_purchase_per_month,
				'phone_number', "Suppliers".phone_number)) from "Suppliers" where phone_number = phone_number0);
		end
	$$;

create or replace function update_supplier(in new_organisation text, in organisation0 text)
	returns void
	language sql
	as $$

	update "Suppliers" set organisation = new_organisation where organisation = organisation0

$$;

/*------------------------------Owners-----------------------------*/

create or replace function add_owner(in name1 text, in foundation_date date, in email text)
	returns void
	language sql
	as $$

	insert into "Owners" (name, foundation_date, email)
    values (name1, foundation_date, email)

$$;

create or replace function delete_owner(in name0 text)
	returns void
	language sql
	as $$

	delete from "Owners" where name = name0

$$;

create or replace function get_owners()
	returns json
	language plpgsql
	as $$
		begin
		   return (select json_agg(json_build_object(
				'name', "Owners".name,
				'foundation_date', "Owners".foundation_date,
				'email', "Owners".email)) from "Owners");
		end
	$$;

create or replace function delete_owners()
	returns void
	language sql
	as $$

	truncate "Owners"

$$;

create or replace function search_owner(in email0 text)
	returns json
	language plpgsql
	as $$
		begin
		   return (select json_agg(json_build_object(
				'name', "Owners".name,
				'foundation_date', "Owners".foundation_date,
				'email', "Owners".email)) from "Owners" where email = email0);
		end
	$$;

create or replace function update_owner(in new_name text, in name0 text)
	returns void
	language sql
	as $$

	update "Owners" set name = new_name where name = name0

$$;

/*--------------------------------------------------------------------*/

/*--------------------------------Lounge_bars--------------------------*/

create or replace function add_lounge_bar(in name text, in address text, in supplier text, in owner text, in common_tobacco text)
	returns void
	language sql
	as $$

	insert into "Lounge_bars"(name,address,supplier,owner,common_tobacco)
    values (name, address, supplier, owner, common_tobacco)

$$;

create or replace function delete_lounge_bar(in name0 text)
	returns void
	language sql
	as $$

	delete from "Lounge_bars" where name = name0

$$;

create or replace function get_lounge_bars()
	returns json
	language plpgsql
	as $$
		begin
		   return (select json_agg(json_build_object(
		        'id', "Lounge_bars".id,
		        'name', "Lounge_bars".name,
				'address', "Lounge_bars".address,
				'supplier', "Lounge_bars".supplier,
				'owner', "Lounge_bars".owner,
				'common_tobacco', "Lounge_bars".common_tobacco)) from "Lounge_bars");
		end
	$$;

create or replace function delete_lounge_bars()
	returns void
	language sql
	as $$

	truncate "Lounge_bars"

$$;

create or replace function search_lounge_bar(in name0 text)
	returns json
	language plpgsql
	as $$
		begin
		   return (select json_agg(json_build_object(
		        'id', "Lounge_bars".id,
		        'name', "Lounge_bars".name,
				'address', "Lounge_bars".address,
				'supplier', "Lounge_bars".supplier,
				'owner', "Lounge_bars".owner,
				'common_tobacco', "Lounge_bars".common_tobacco)) from "Lounge_bars" where name = name0);
		end
	$$;

create or replace function update_lounge_bar(in new_name text, in name0 text)
	returns void
	language sql
	as $$

	update "Lounge_bars" set name = new_name where name = name0

$$;

/*--------------------------------------------------------------------------*/